# -*- coding: utf-8 -*-
# Time     :2024/1/22 00:36
# Author   :ym
# File     :bera_tools.py
import json
import random
import time
from typing import Union
import configparser
import requests
from eth_account import Account
from eth_typing import Address, ChecksumAddress
from faker import Faker
from requests import Response
from solcx import compile_source, set_solc_version, compile_standard
from web3 import Web3
from loguru import logger

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from config.abi_config import erc_20_abi, honey_abi, bex_abi, bend_abi, bend_borrows_abi, ooga_booga_abi, nft_abi, \
    domain_abi
from config.address_config import bex_swap_address, usdc_address, honey_address, honey_swap_address, \
    bex_approve_liquidity_address, weth_address, bend_address, bend_borrows_address, wbear_address, zero_address, \
    ooga_booga_address, aweth_address, ahoney_address, vdhoney_address, nft_address, nft2_address, domain_address

gas_rate = 1.2
wait_time_out = 60


def get_app_item(values, index):
    if index in values:
        k = values[index]
    else:
        k = ''
    return k


config = configparser.ConfigParser()
config.read('config.ini')
app = config._sections['app']
file_path = get_app_item(app, 'file_path')
rpc_url = get_app_item(app, 'rpc_url')
proxy_url = get_app_item(app, 'proxy_url')
solver_provider = get_app_item(app, 'solver_provider')
client_key = get_app_item(app, 'client_key')
proxy_mode = get_app_item(app, 'proxy_mode')
proxy_list = get_app_item(app, 'proxy_list')


def get_proxy():
    if proxy_mode == 'smart':
        proxy = {
            'http': proxy_list,
            'https': proxy_list
        }
    else:
        aaa = requests.get(proxy_url, verify=False, proxies={}).text
        proxy_host = aaa.splitlines()[0]
        proxy = {
            'http': 'http://' + proxy_host,
            'https': 'http://' + proxy_host
        }
    # logger.debug(f'代理IP为:{proxy}')
    return proxy


class BeraChainTools(object):
    def __init__(self, private_key,
                 proxy_url=proxy_url,
                 client_key=client_key,
                 solver_provider=solver_provider,
                 rpc_url='https://artio.rpc.berachain.com/'
                 ):
        # if solver_provider is None:
        #     print('None')
        # if solver_provider not in ["yescaptcha", "2captcha", "ez-captcha", ""]:
        #     raise ValueError("solver_provider must be 'yescaptcha' or '2captcha' or 'ez-captcha' ")
        self.solver_provider = solver_provider
        self.private_key = private_key
        self.client_key = client_key
        self.rpc_url = rpc_url
        self.proxy_url = proxy_url
        self.fake = Faker()
        self.account = Account.from_key(self.private_key)
        self.session = requests.session()
        self.w3 = Web3(Web3.HTTPProvider(endpoint_uri=self.rpc_url))
        self.bex_contract = self.w3.eth.contract(address=bex_swap_address, abi=bex_abi)
        self.honey_swap_contract = self.w3.eth.contract(address=honey_swap_address, abi=honey_abi)
        self.usdc_contract = self.w3.eth.contract(address=usdc_address, abi=erc_20_abi)
        self.weth_contract = self.w3.eth.contract(address=weth_address, abi=erc_20_abi)
        self.honey_contract = self.w3.eth.contract(address=honey_address, abi=erc_20_abi)
        self.bend_contract = self.w3.eth.contract(address=bend_address, abi=bend_abi)
        self.bend_borrows_contract = self.w3.eth.contract(address=bend_borrows_address, abi=bend_borrows_abi)
        self.ooga_booga_contract = self.w3.eth.contract(address=ooga_booga_address, abi=ooga_booga_abi)
        self.aweth_contract = self.w3.eth.contract(address=aweth_address, abi=erc_20_abi)
        self.ahoney_contract = self.w3.eth.contract(address=ahoney_address, abi=erc_20_abi)
        # 借贷的凭据
        self.vdhoney_contract = self.w3.eth.contract(address=vdhoney_address, abi=erc_20_abi)
        self.nft_contract = self.w3.eth.contract(address=nft_address, abi=nft_abi)
        self.nft2_contract = self.w3.eth.contract(address=nft2_address, abi=nft_abi)
        self.domain_contract = self.w3.eth.contract(address=domain_address, abi=domain_abi)
        # print(self.rpc_url)

    # def get_2captcha_google_token(self) -> Union[bool, str]:
    #     if self.client_key == '':
    #         raise ValueError('2captcha_client_key is null ')
    #     params = {'key': self.client_key, 'method': 'userrecaptcha', 'version': 'v3', 'action': 'submit',
    #               'min_score': 0.5,
    #               'googlekey': '6LfOA04pAAAAAL9ttkwIz40hC63_7IsaU2MgcwVH',
    #               'pageurl': 'https://artio.faucet.berachain.com/',
    #               'json': 1}
    #     response = requests.get(f'https://2captcha.com/in.php?', params=params).json()
    #     if response['status'] != 1:
    #         raise ValueError(response)
    #     task_id = response['request']
    #     for _ in range(60):
    #         response = requests.get(
    #             f'https://2captcha.com/res.php?key={self.client_key}&action=get&id={task_id}&json=1').json()
    #         if response['status'] == 1:
    #             return response['request']
    #         else:
    #             time.sleep(3)
    #     return False

    def get_2captcha_google_token(self) -> Union[bool, str]:
        if self.client_key == '':
            raise ValueError('2captcha_client_key is null ')
        # params = {
        #     'key': self.client_key,
        #     'method': 'userrecaptcha',
        #     'version': 'v3',
        #     'action': 'submit',
        #           'min_score': 0.5,
        #           'googlekey': '6LfOA04pAAAAAL9ttkwIz40hC63_7IsaU2MgcwVH',
        #           'pageurl': 'https://artio.faucet.berachain.com/',
        #           'json': 1
        # }
        params = {
            "method": "turnstile",
            "key": self.client_key,
            "sitekey": "0x4AAAAAAARdAuciFArKhVwt",
            "pageurl": "https://artio.faucet.berachain.com/",
            "json": 1
        }
        response = requests.get(f'https://2captcha.com/in.php?', params=params, verify=False).json()
        if response['status'] != 1:
            raise ValueError(response)
        task_id = response['request']
        for _ in range(60):
            response = requests.get(
                f'https://2captcha.com/res.php?key={self.client_key}&action=get&id={task_id}&json=1',
                verify=False).json()
            if response['status'] == 1:
                return response['request']
            else:
                time.sleep(3)
        return False

    def get_yescaptcha_google_token(self) -> Union[bool, str]:
        if self.client_key == '':
            raise ValueError('yes_captcha_client_key is null ')
        json_data = {"clientKey": self.client_key,
                     "task": {"websiteURL": "https://artio.faucet.berachain.com/",
                              "websiteKey": "6LfOA04pAAAAAL9ttkwIz40hC63_7IsaU2MgcwVH",
                              "type": "RecaptchaV3TaskProxylessM1S7", "pageAction": "submit"}, "softID": 109}
        response = self.session.post(url='https://api.yescaptcha.com/createTask', json=json_data, verify=False).json()
        if response['errorId'] != 0:
            raise ValueError(response)
        task_id = response['taskId']
        time.sleep(5)
        for _ in range(30):
            data = {"clientKey": self.client_key, "taskId": task_id}
            response = requests.post(url='https://api.yescaptcha.com/getTaskResult', json=data, verify=False).json()
            if response['status'] == 'ready':
                return response['solution']['gRecaptchaResponse']
            else:
                time.sleep(2)
        return False

    # def get_ez_captcha_google_token(self) -> Union[bool, str]:
    #     if self.client_key == '':
    #         raise ValueError('ez-captcha is null ')
    #     json_data = {
    #         "clientKey": self.client_key,
    #         "task": {"websiteURL": "https://artio.faucet.berachain.com/",
    #                  "websiteKey": "6LfOA04pAAAAAL9ttkwIz40hC63_7IsaU2MgcwVH",
    #                  "type": "ReCaptchaV3TaskProxyless", }, 'appId': '34119'}
    #     response = self.session.post(url='https://api.ez-captcha.com/createTask', json=json_data).json()
    #     if response['errorId'] != 0:
    #         logger.error(f'获取google token 出错，{response}')
    #         raise ValueError(response)
    #     task_id = response['taskId']
    #     time.sleep(5)
    #     for _ in range(30):
    #         data = {"clientKey": self.client_key, "taskId": task_id}
    #         response = requests.post(url='https://api.ez-captcha.com/getTaskResult', json=data).json()
    #         if response['status'] == 'ready':
    #             return response['solution']['gRecaptchaResponse']
    #         else:
    #             time.sleep(2)
    #     return False
    def get_ez_captcha_google_token(self) -> Union[bool, str]:
        if self.client_key == '':
            raise ValueError('ez-captcha is null ')
        json_data = {
            "clientKey": self.client_key,
            "task": {"websiteURL": "https://artio.faucet.berachain.com/",
                     "websiteKey": "6LfOA04pAAAAAL9ttkwIz40hC63_7IsaU2MgcwVH",
                     "type": "ReCaptchaV3TaskProxyless", }, 'appId': '34119'}
        response = self.session.post(url='https://api.ez-captcha.com/createTask', json=json_data, verify=False).json()
        if response['errorId'] != 0:
            raise ValueError(response)
        task_id = response['taskId']
        time.sleep(5)
        for _ in range(30):
            data = {"clientKey": self.client_key, "taskId": task_id}
            response = requests.post(url='https://api.ez-captcha.com/getTaskResult', json=data, verify=False).json()
            if response['status'] == 'ready':
                return response['solution']['gRecaptchaResponse']
            else:
                time.sleep(2)
        return False

    def get_gas_price(self):
        return self.w3.eth.gas_price

    def get_nonce(self):
        noncelist = []
        for i in range(10):
            nonce = self.w3.eth.get_transaction_count(self.account.address)
            noncelist.append(nonce)
        return max(noncelist)

    def get_balance(self):
        return self.w3.eth.get_balance(self.account.address)

    def get_solver_provider(self):
        provider_dict = {
            'yescaptcha': self.get_yescaptcha_google_token,
            '2captcha': self.get_2captcha_google_token,
            'ez-captcha': self.get_ez_captcha_google_token,
        }
        if self.solver_provider not in list(provider_dict.keys()):
            raise ValueError("solver_provider must be 'yescaptcha' or '2captcha' or 'ez-captcha' ")
        return provider_dict[self.solver_provider]()

    # 处理错误消息

    def claim_bera(self, proxies=None) -> Response:
        """
        bera领水
        :param proxies: http代理
        :return: object
        """
        # print('领水')
        google_token = self.get_solver_provider()
        if not google_token:
            raise ValueError('获取google token 出错')
        user_agent = self.fake.chrome()
        # url = 'https://artio-80085-faucet-api-recaptcha.berachain.com/api/claim'
        # host = 'artio-80085-faucet-api-recaptcha.berachain.com'
        # headers = {
        #     'authority': host,
        #     'accept': '*/*',
        #     'accept-language': 'zh-CN,zh;q=0.9',
        #     'authorization': f'Bearer {google_token}',
        #     'cache-control': 'no-cache',
        #     'content-type': 'text/plain;charset=UTF-8',
        #     'origin': 'https://artio.faucet.berachain.com',
        #     'pragma': 'no-cache',
        #     'referer': 'https://artio.faucet.berachain.com/',
        #     'user-agent': user_agent
        # }
        url = 'https://artio-80085-faucet-api-cf.berachain.com/api/claim'
        host = 'artio-80085-faucet-api-cf.berachain.com'
        headers = {
            'authority': host,
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'authorization': f'Bearer {google_token}',
            'cache-control': 'no-cache',
            'content-type': 'text/plain;charset=UTF-8',
            'origin': 'https://artio.faucet.berachain.com',
            'pragma': 'no-cache',
            'referer': 'https://artio.faucet.berachain.com/',
            'user-agent': user_agent
        }
        params = {'address': self.account.address}
        proxies = get_proxy()
        for i in range(10):
            try:
                response = requests.post(url,
                                         params=params,
                                         headers=headers,
                                         data=json.dumps(params),
                                         proxies=proxies,
                                         timeout=30,
                                         verify=False
                                         )
                return response
            except Exception as e:
                logger.debug(f'第{i}次使用代理{proxies["http"]},错误代码,{e}')
                proxies = get_proxy()

    def deal_with_e_message(self, e):
        if 'insufficient funds for gas' in str(e):
            self.claim_bera()

    def approve_token(self, spender: Union[Address, ChecksumAddress], amount: int,
                      approve_token_address: Union[Address, ChecksumAddress]) -> bool:
        """
        授权代币
        :param spender: 授权给哪个地址
        :param amount: 授权金额
        :param approve_token_address: 需要授权的代币地址
        :return: hash
        """
        try:
            approve_contract = self.w3.eth.contract(address=approve_token_address, abi=erc_20_abi)
            allowance_balance = approve_contract.functions.allowance(self.account.address, spender).call()
            if allowance_balance > amount:
                logger.debug(f'已授权,无须重复授权！')
                return True
                # 无限授权
                # approve_amount = 0
                # if spender == nft_address:
                #     approve_amount = 18*10**18
                # else:
            approve_amount = int("0x" + "f" * 64, 16)
            txn = approve_contract.functions.approve(spender, approve_amount).build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                # logger.debug(f'授权成功,{transaction_receipt.status}')
                return True
            else:
                # logger.debug(f'授权失败,{transaction_receipt.status}')
                return False
        except Exception as e:
            print('approve_token', self.account.address, e)
            return False

    def bex_swap(self, amount_in: int, asset_in_address: Union[Address, ChecksumAddress],
                 asset_out_address: Union[Address, ChecksumAddress]) -> bool:
        """
        bex 交换
        :param amount_in: 输入数量
        :param asset_in_address: 输入 token 地址
        :param asset_out_address: 输出 token 地址
        :return:
        """
        try:
            if asset_in_address == wbear_address:
                balance = self.w3.eth.get_balance(self.account.address)
                assert balance != 0
                assert balance >= amount_in
            else:
                asset_in_token_contract = self.w3.eth.contract(address=asset_in_address, abi=erc_20_abi)
                balance = asset_in_token_contract.functions.balanceOf(self.account.address).call()
                assert balance != 0
                assert balance >= amount_in
            swaps = list()
            if asset_in_address == wbear_address and asset_out_address == usdc_address:
                swaps.append(dict(
                    poolId='0x7D5b5C1937ff1b18B45AbC64aeAB68663a7a58Ab',
                    assetIn='0x0000000000000000000000000000000000000000',
                    amountIn=amount_in,
                    assetOut=usdc_address,
                    amountOut=0,
                    userData=b''
                ))
            elif asset_in_address == wbear_address and asset_out_address == weth_address:
                swaps.append(dict(
                    poolId='0xD3C962F3F36484439A41d0E970cF6581dDf0a9A1',
                    assetIn='0x0000000000000000000000000000000000000000',
                    amountIn=amount_in,
                    assetOut=weth_address,
                    amountOut=0,
                    userData=b''
                ))
            elif asset_in_address == usdc_address and asset_out_address == honey_address:
                swaps.append(dict(
                    poolId='0x5479FbDef04302D2DEEF0Cc78f7D503d81fDFCC9',
                    assetIn=usdc_address,
                    amountIn=amount_in,
                    assetOut=honey_address,
                    amountOut=0,
                    userData=b''
                ))
            else:
                return False

            txn = self.bex_contract.functions.batchSwap(kind=0, swaps=swaps, deadline=99999999).build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    'value': amount_in if asset_in_address == wbear_address else 0,
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            # 等待交易收据
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                # logger.debug(f'交换成功,{transaction_receipt.status}')
                return True
            else:
                # logger.debug(f'交换失败,{transaction_receipt.status}')
                return False
        except Exception as e:
            print('bex_swap', self.account.address, e)
            return False

    def bex_add_liquidity(self, amount_in: int, pool_address: Union[Address], asset_in_address: Union[Address]) -> bool:
        """
        bex 增加流动性
        :param amount_in: 输入数量
        :param pool_address: 交互的pool 地址
        :param asset_in_address: 需要加流动性的token地址
        :return:
        """
        try:
            asset_in_token_contract = self.w3.eth.contract(address=asset_in_address, abi=erc_20_abi)
            token_balance = asset_in_token_contract.functions.balanceOf(self.account.address).call()
            assert token_balance != 0
            assert token_balance >= amount_in
            txn = self.bex_contract.functions.addLiquidity(pool=pool_address, receiver=self.account.address,
                                                           assetsIn=[asset_in_address],
                                                           amountsIn=[amount_in]).build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                # logger.debug(f'bex 增加流动性成功,{transaction_receipt.status}')
                return True
            else:
                # logger.debug(f'bex 增加流动性失败,{transaction_receipt.status}')
                return False
        except Exception as e:
            print('bex_add_liquidity', self.account.address, e)
            return False

    def honey_mint(self, amount_usdc_in: int) -> bool:
        """
        honey mint
        :param amount_usdc_in: 输入数量
        :return:
        """
        try:
            usdc_balance = self.usdc_contract.functions.balanceOf(self.account.address).call()
            assert usdc_balance != 0
            assert usdc_balance >= amount_usdc_in
            txn = self.honey_swap_contract.functions.mint(to=self.account.address, collateral=usdc_address,
                                                          amount=amount_usdc_in, ).build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                return True
            else:
                return False
        except Exception as e:
            print('honey_mint', self.account.address, e)
            return False

    def honey_redeem(self, amount_honey_in: int) -> bool:
        """
        honey redeem
        :param amount_honey_in: 输入数量
        :return:
        """
        try:
            honey_balance = self.honey_contract.functions.balanceOf(self.account.address).call()
            assert honey_balance != 0
            assert honey_balance >= amount_honey_in
            txn = self.honey_swap_contract.functions.redeem(to=self.account.address, amount=amount_honey_in,
                                                            collateral=usdc_address).build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                return True
            else:
                return False
        except Exception as e:
            print('honey_redeem', self.account.address, e)
            return False

    def bend_deposit(self, amount_in: int, amount_in_token_address: Union[Address]) -> bool:
        """
        bend deposit
        :param amount_in: 数量
        :param amount_in_token_address: 代币地址
        :return:
        """
        try:
            amount_in_token_contract = self.w3.eth.contract(address=amount_in_token_address, abi=erc_20_abi)
            token_balance = amount_in_token_contract.functions.balanceOf(self.account.address).call()
            assert token_balance != 0
            assert token_balance >= amount_in
            txn = self.bend_contract.functions.supply(asset=amount_in_token_address, amount=amount_in,
                                                      onBehalfOf=self.account.address,
                                                      referralCode=0).build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                return True
            else:
                return False
        except Exception as e:
            print('bend_deposit', self.account.address, e)
            return False

    def bend_borrow(self, amount_out: int, asset_token_address: Union[Address]) -> bool:
        """
        bend borrow
        :param amount_out: 数量
        :param asset_token_address: 借款代币地址
        :return:
        """
        try:
            txn = self.bend_contract.functions.borrow(asset=asset_token_address, amount=amount_out,
                                                      interestRateMode=2, referralCode=0,
                                                      onBehalfOf=self.account.address).build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                return True
            else:
                return False
        except Exception as e:
            print('bend_borrow', self.account.address, e)
            return False

    def bend_repay(self, repay_amount: int, asset_token_address: Union[Address]) -> bool:
        """
        bend 还款
        :param repay_amount:还款数量
        :param asset_token_address: repay 代币地址
        :return:
        """
        try:
            txn = self.bend_contract.functions.repay(asset=asset_token_address, amount=repay_amount,
                                                     interestRateMode=2,
                                                     onBehalfOf=self.account.address).build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                return True
            else:
                return False
        except Exception as e:
            print('bend_repay', self.account.address, e)
            return False

    def honey_jar_mint(self):
        try:
            has_mint = self.ooga_booga_contract.functions.hasMinted(self.account.address).call()
            if has_mint:
                # logger.debug(f'已mint！')
                return True
            signed_txn = self.w3.eth.account.sign_transaction(
                dict(
                    chainId=80085,
                    nonce=self.get_nonce(),
                    gasPrice=int(self.w3.eth.gas_price * gas_rate),
                    gas=134500 + random.randint(1, 10000),
                    to=self.w3.to_checksum_address(ooga_booga_address),
                    data='0xa6f2ae3a',
                ),
                self.account.key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                # logger.debug(f'mint成功,{transaction_receipt.status}')
                return True
            else:
                # logger.debug(f'mint失败,{transaction_receipt.status}')
                return False
        except Exception as e:
            print('honey_jar_mint', self.account.address, e)
            return False

    def nft_mint(self):
        try:
            has_mint = self.nft_contract.functions.hasMinted(self.account.address).call()
            if has_mint:
                # logger.debug(f'已mint！')
                return True
            txn = self.nft_contract.functions.buy().build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                # logger.debug(f'mint成功,{transaction_receipt.status}')
                return True
            else:
                # logger.debug(f'mint失败,{transaction_receipt.status}')
                return False
        except Exception as e:
            print('nft_mint', self.account.address, e)
            return False

    def nft2_mint(self):
        try:
            has_mint = self.nft2_contract.functions.hasMinted(self.account.address).call()
            if has_mint:
                # logger.debug(f'已mint！')
                return True
            txn = self.nft2_contract.functions.buy().build_transaction(
                {
                    'from': self.account.address,
                    # 'gas': 500000 + random.randint(1, 10000),
                    # 'gasPrice': int(self.w3.eth.gas_price * gas_rate),
                    'nonce': self.get_nonce()
                })
            signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                # logger.debug(f'mint成功,{transaction_receipt.status}')
                return True
            else:
                # logger.debug(f'mint失败,{transaction_receipt.status}')
                return False
        except Exception as e:
            print('nft2_mint', self.account.address, e)
            return False

    def send_bera20(self):
        try:
            transaction = dict(
                chainId=80085,
                nonce=self.get_nonce(),
                gasPrice=int(self.w3.eth.gas_price * gas_rate),
                to=self.w3.to_checksum_address(self.account.address),
                data='0x646174613a2c7b2270223a22626572612d3230222c226f70223a226d696e74222c227469636b223a224245524173222c22616d74223a2231303030227d',
            )
            gas_estimate = self.w3.eth.estimate_gas(transaction)
            gas_limit = gas_estimate + random.randint(1, 10000)
            transaction['gas'] = gas_limit
            signed_txn = self.w3.eth.account.sign_transaction(
                transaction,
                self.account.key
            )
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            # return True
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                # logger.debug(f'mint成功,{transaction_receipt.status}')
                return True
            else:
                # logger.debug(f'mint失败,{transaction_receipt.status}')
                return False
        except Exception as e:
            print('send_bera20', self.account.address, e)
            return False

    def create_domain(self):
        try:
            converted_d = [
                "\U0001f642", "\U0001f600", "\U0001f604", "\U0001f601", "\U0001f606", "\U0001f605", "\U0001f923",
                "\U0001f603",
                "\U0001f972", "\U0001f60b", "\U0001f61b", "\U0001f61d", "\U0001f61c", "\U0001f9aa", "\U0001f9a8",
                "\U0001fad0",
                "\U0001f913", "\U0001f60e", "\U0001f615", "\U0001f641", "\U0001f623", "\U0001f616", "\U0001f62b",
                "\U0001f629",
                "\U0001f97a", "\U0001f622", "\U0001f62d", "\U0001f624", "\U0001f620", "\U0001f621", "\U0001f9ac",
                "\U0001f9af",
                "\U0001f633", "\U0001f975", "\U0001f976", "\U0001f631", "\U0001f628", "\U0001f630", "\U0001f625",
                "\U0001f613",
                "\U0001f617", "\U0001f627", "\U0001f62e", "\U0001f632", "\U0001f634", "\U0001f924", "\U0001f62a",
                "\U0001f971",
                "\U0001f922", "\U0001f92e", "\U0001f927", "\U0001f974", "\U0001f637", "\U0001f912", "\U0001f915",
                "\U0001f911",
                "\U0001f920", "\U0001f608", "\U0001f47f", "\U0001f479", "\U0001f47a", "\U0001f921", "\U0001f4a9",
                "\U0001f47b",
                "\U0001f480", "\U0001f47d", "\U0001f47e", "\U0001f916", "\U0001f383"
            ]

            converted_e = [
                "\U0001f41d", "\U0001f435", "\U0001f412", "\U0001f98d", "\U0001f9a7", "\U0001f436", "\U0001f415",
                "\U0001f9ae",
                "\U0001f429", "\U0001f43a", "\U0001f98a", "\U0001f99d", "\U0001f431", "\U0001f408",
                "\U0001f981", "\U0001f42f", "\U0001f405", "\U0001f406", "\U0001f434", "\U0001f40e", "\U0001f984",
                "\U0001f993",
                "\U0001f98c", "\U0001f42e", "\U0001f402", "\U0001f403", "\U0001f404", "\U0001f437", "\U0001f416",
                "\U0001f417",
                "\U0001f43d", "\U0001f40f", "\U0001f411", "\U0001f410", "\U0001f999", "\U0001f992", "\U0001f418",
                "\U0001f98f",
                "\U0001f99b", "\U0001f42d", "\U0001f401", "\U0001f400", "\U0001f439", "\U0001f430", "\U0001f407",
                "\U0001f43f\uFE0F", "\U0001f994", "\U0001f987", "\U0001f43b", "\U0001f428", "\U0001f43c", "\U0001f9a5",
                "\U0001f9a6", "\U0001f9a8",
                "\U0001f998", "\U0001f9a1", "\U0001f93e", "\U0001f93f", "\U0001f525", "\U0001f308"
            ]

            converted_f = [
                "\U0001F3EF", "\U0001F347", "\U0001F348", "\U0001F349", "\U0001F34A", "\U0001F34B", "\U0001F34C",
                "\U0001F34D",
                "\U0001F96D", "\U0001F34E", "\U0001F34F", "\U0001F350", "\U0001F351", "\U0001F352", "\U0001F353",
                "\U0001F3F0",
                "\U0001F55D", "\U0001F345", "\U0001F3D2", "\U0001F365", "\U0001F351", "\U0001F546", "\U0001F346",
                "\U0001F554",
                "\U0001F555", "\U0001F33D", "\U0001F336", "\U0001F3D1", "\U0001F352", "\U0001F36C", "\U0001F366",
                "\U0001F3C4",
                "\U0001F3C5", "\U0001F344", "\U0001F55C", "\U0001F3D1", "\U0001F550", "\U0001F556", "\U0001F3D3",
                "\U0001F368",
                "\U0001F36F", "\U0001F55E", "\U0001F356", "\U0001F357", "\U0001F369", "\U0001F353", "\U0001F354",
                "\U0001F32D",
                "\U0001F36A", "\U0001F32E", "\U0001F32F", "\U0001F3D4", "\U0001F359", "\U0001F3C6", "\U0001F35A",
                "\U0001F573",
                "\U0001F358", "\U0001F372", "\U0001F3D5", "\U0001F363", "\U0001F357", "\U0001F37F", "\U0001F36B",
                "\U0001F371",
                "\U0001F358", "\U0001F359", "\U0001F35A"]

            combined_list = converted_d + converted_e + converted_f
            # 注意去重
            combined_list = list(set(combined_list))
            domain_len_list = [5, 6, 7, 8]
            domain_len = random.choice(domain_len_list)
            random_selection = random.sample(combined_list, domain_len)
            # gas = int(self.w3.eth.gas_price * gas_rate)
            transaction = self.domain_contract.functions.mintNative(random_selection, 1, self.account.address,
                                                                    "https://beranames.com/api/metadata/69",
                                                                    self.account.address).build_transaction(
                {
                    'from': self.account.address,
                    'nonce': self.get_nonce(),
                    'value': int(608610 * 10 ** 9)
                })
            signed_txn = self.w3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(transaction_hash=order_hash,
                                                                           timeout=wait_time_out)
            if transaction_receipt.status == 1:
                return True
            else:
                return False
        except Exception as e:
            print('create_domain', self.account.address, e)
            return False

    def deploy_contract(self, contract_source_code, solc_version):
        """
        部署合约
        运行前需要安装你指定的版本
            from solcx import install_solc
            install_solc('0.4.18')
        :param contract_source_code: 合约代码
        :param solc_version: 编译器版本
        :return:
        """
        ""
        try:
            set_solc_version(solc_version)
            compiled_sol = compile_source(contract_source_code, optimize=True)
            contract_id, contract_interface = compiled_sol.popitem()
            gas_price = int(self.w3.eth.gas_price * gas_rate)
            transaction = dict(
                chainId=80085,
                gasPrice=gas_price,
                nonce=self.get_nonce(),
                data=contract_interface['bin']
            )
            gas_estimate = self.w3.eth.estimate_gas(transaction)
            gas_limit = gas_estimate + random.randint(1, 10000)
            transaction['gas'] = gas_limit
            signed_txn = self.w3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash, timeout=wait_time_out)
            if transaction_receipt.status == 1:
                return True
            else:
                return False
        except Exception as e:
            print('deploy_contract', self.account.address, e)
            return False
