# -*- coding: utf-8 -*-
# Time     :2024/1/22 00:36
# Author   :ym
# File     :bera_tools.py
import json
import random
import time
from typing import Union
import requests
from eth_account import Account
from eth_typing import Address, ChecksumAddress
from faker import Faker
from requests import Response
from solcx import compile_source, set_solc_version
from web3 import Web3
from loguru import logger

from config.abi_config import erc_20_abi, honey_abi, bex_abi, bend_abi, bend_borrows_abi, ooga_booga_abi, nft_abi
from config.address_config import bex_swap_address, usdc_address, honey_address, honey_swap_address, \
    bex_approve_liquidity_address, weth_address, bend_address, bend_borrows_address, wbear_address, zero_address, \
    ooga_booga_address, aweth_address, ahoney_address, vdhoney_address, nft_address, nft2_address


def get_proxy(proxy_url):
    aaa = requests.get(proxy_url).text
    proxy_host = aaa.splitlines()[0]
    logger.debug('代理IP为：' + proxy_host)
    proxy = {
        'http': 'http://' + proxy_host,
        'https': 'http://' + proxy_host
    }
    return proxy


class BeraChainTools(object):
    def __init__(self, private_key,
                 proxy_url='',
                 client_key='',
                 solver_provider='',
                 rpc_url='https://artio.rpc.berachain.com/'
                 ):
        if solver_provider not in ["yescaptcha", "2captcha", "ez-captcha", ""]:
            raise ValueError("solver_provider must be 'yescaptcha' or '2captcha' or 'ez-captcha' ")
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
        response = requests.get(f'https://2captcha.com/in.php?', params=params).json()
        if response['status'] != 1:
            raise ValueError(response)
        task_id = response['request']
        for _ in range(60):
            response = requests.get(
                f'https://2captcha.com/res.php?key={self.client_key}&action=get&id={task_id}&json=1').json()
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
        response = self.session.post(url='https://api.yescaptcha.com/createTask', json=json_data).json()
        if response['errorId'] != 0:
            raise ValueError(response)
        task_id = response['taskId']
        time.sleep(5)
        for _ in range(30):
            data = {"clientKey": self.client_key, "taskId": task_id}
            response = requests.post(url='https://api.yescaptcha.com/getTaskResult', json=data).json()
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
        response = self.session.post(url='https://api.ez-captcha.com/createTask', json=json_data).json()
        if response['errorId'] != 0:
            raise ValueError(response)
        task_id = response['taskId']
        time.sleep(5)
        for _ in range(30):
            data = {"clientKey": self.client_key, "taskId": task_id}
            response = requests.post(url='https://api.ez-captcha.com/getTaskResult', json=data).json()
            if response['status'] == 'ready':
                return response['solution']['gRecaptchaResponse']
            else:
                time.sleep(2)
        return False

    def get_nonce(self):
        noncelist = []
        for i in range(5):
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

    def claim_bera(self, proxies=None) -> Response:
        """
        bera领水
        :param proxies: http代理
        :return: object
        """
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
        for i in range(10):
            try:
                response = requests.post(url,
                                         params=params,
                                         headers=headers,
                                         data=json.dumps(params),
                                         proxies=proxies,
                                         timeout=30
                                         )
                logger.debug(f'第{i}次使用代理{proxies["http"]},返回结果,{response.text}')
                return response
            except Exception as e:
                logger.debug(f'第{i}次使用代理{proxies["http"]},错误代码,{e}')
                proxies = get_proxy(self.proxy_url)

    def approve_token(self, spender: Union[Address, ChecksumAddress], amount: int,
                      approve_token_address: Union[Address, ChecksumAddress]) -> bool:
        """
        授权代币
        :param spender: 授权给哪个地址
        :param amount: 授权金额
        :param approve_token_address: 需要授权的代币地址
        :return: hash
        """
        # if spender == nft_address:
        #     signed_txn = self.w3.eth.account.sign_transaction(
        #         dict(
        #             chainId=80085,
        #             nonce=self.get_nonce(),
        #             gasPrice=int(self.w3.eth.gas_price * 1.15),
        #             gas=134500 + random.randint(1, 10000),
        #             to=self.w3.to_checksum_address(approve_token_address),
        #             data='0x095ea7b3000000000000000000000000dc094eac7cc01224e798f34543a8f9e9d25594790000000000000000000000000000000000000000000000056bc75e2d63100000',  # 0xa6f2ae3a
        #         ),
        #         self.account.key)
        #     order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        #     transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        #     if transaction_receipt.status == 1:
        #         # logger.debug(f'授权成功,{transaction_receipt.status}')
        #         return True
        #     else:
        #         # logger.debug(f'授权失败,{transaction_receipt.status}')
        #         return False
        # # if spender == nft_address:
        # #     amount = 18
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
                'gas': 500000 + random.randint(1, 10000),
                'gasPrice': int(self.w3.eth.gas_price * 1.15),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            # logger.debug(f'授权成功,{transaction_receipt.status}')
            return True
        else:
            # logger.debug(f'授权失败,{transaction_receipt.status}')
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
        if asset_in_address == wbear_address:
            balance = self.w3.eth.get_balance(self.account.address)
            assert balance != 0
            assert balance >= amount_in
        else:
            asset_in_token_contract = self.w3.eth.contract(address=asset_in_address, abi=erc_20_abi)
            balance = asset_in_token_contract.functions.balanceOf(self.account.address).call()
            assert balance != 0
            assert balance >= amount_in
        #     allowance_balance = asset_in_token_contract.functions.allowance(self.account.address,
        #                                                                     bex_swap_address).call()
        #     if allowance_balance < amount_in:
        #         raise ValueError(
        #             f'需要授权\nplease run : \nbera.approve_token(bex_swap_address, int("0x" + "f" * 64, 16), "{asset_in_address}")')
        #
        # headers = {'authority': 'artio-80085-dex-router.berachain.com', 'accept': '*/*',
        #            'accept-language': 'zh-CN,zh;q=0.9', 'cache-control': 'no-cache',
        #            'origin': 'https://artio.bex.berachain.com', 'pragma': 'no-cache',
        #            'referer': 'https://artio.bex.berachain.com/', 'user-agent': self.fake.chrome()}
        #
        # params = {'quoteAsset': asset_out_address, 'baseAsset': asset_in_address, 'amount': amount_in,
        #           'swap_type': 'given_in'}
        #
        # response = self.session.get('https://artio-80085-dex-router.berachain.com/dex/route', params=params,
        #                             headers=headers)
        # # print(params)
        # print(response.text)
        # assert response.status_code == 200
        # swaps_list = response.json()['steps']
        swaps = list()
        # for index, info in enumerate(swaps_list):
        #     swaps.append(dict(
        #         poolId=self.w3.to_checksum_address(info['pool']),
        #         assetIn=self.w3.to_checksum_address(info['assetIn']),
        #         amountIn=int(info['amountIn']),
        #         assetOut=self.w3.to_checksum_address(info['assetOut']),
        #         # amountOut=0 if index + 1 != len(swaps_list) else int(int(info['amountOut']) * 0.4),
        #         amountOut=0,
        #         userData=b''))
        # if asset_in_address.lower() == wbear_address.lower():
        #     swaps[0]['assetIn'] = zero_address
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
            # logger.debug(f'交换失败,不支持的交易')
            return False

        # print(swaps)

        txn = self.bex_contract.functions.batchSwap(kind=0, swaps=swaps, deadline=99999999).build_transaction(
            {
                'gas': 500000 + random.randint(1, 10000),
                'value': amount_in if asset_in_address == wbear_address else 0,
                'gasPrice': int(self.w3.eth.gas_price * 1.2),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        # 等待交易收据
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            # logger.debug(f'交换成功,{transaction_receipt.status}')
            return True
        else:
            # logger.debug(f'交换失败,{transaction_receipt.status}')
            return False

    def bex_add_liquidity(self, amount_in: int, pool_address: Union[Address], asset_in_address: Union[Address]) -> bool:
        """
        bex 增加流动性
        :param amount_in: 输入数量
        :param pool_address: 交互的pool 地址
        :param asset_in_address: 需要加流动性的token地址
        :return:
        """
        asset_in_token_contract = self.w3.eth.contract(address=asset_in_address, abi=erc_20_abi)
        token_balance = asset_in_token_contract.functions.balanceOf(self.account.address).call()
        assert token_balance != 0
        assert token_balance >= amount_in
        txn = self.bex_contract.functions.addLiquidity(pool=pool_address, receiver=self.account.address,
                                                       assetsIn=[asset_in_address],
                                                       amountsIn=[amount_in]).build_transaction(
            {
                'gas': 500000 + random.randint(1, 10000),
                'gasPrice': int(self.w3.eth.gas_price * 1.15),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            # logger.debug(f'bex 增加流动性成功,{transaction_receipt.status}')
            return True
        else:
            # logger.debug(f'bex 增加流动性失败,{transaction_receipt.status}')
            return False

    def honey_mint(self, amount_usdc_in: int) -> bool:
        """
        honey mint
        :param amount_usdc_in: 输入数量
        :return:
        """
        usdc_balance = self.usdc_contract.functions.balanceOf(self.account.address).call()
        assert usdc_balance != 0
        assert usdc_balance >= amount_usdc_in
        txn = self.honey_swap_contract.functions.mint(to=self.account.address, collateral=usdc_address,
                                                      amount=amount_usdc_in, ).build_transaction(
            {
                'gas': 500000 + random.randint(1, 10000),
                'gasPrice': int(self.w3.eth.gas_price * 1.15),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            return True
        else:
            return False
        # logger.debug(f'STGUSDC转换HONEY成功,{transaction_receipt.status}')
        # return order_hash.hex()

    def honey_redeem(self, amount_honey_in: int) -> bool:
        """
        honey redeem
        :param amount_honey_in: 输入数量
        :return:
        """
        honey_balance = self.honey_contract.functions.balanceOf(self.account.address).call()
        assert honey_balance != 0
        assert honey_balance >= amount_honey_in
        txn = self.honey_swap_contract.functions.redeem(to=self.account.address, amount=amount_honey_in,
                                                        collateral=usdc_address).build_transaction(
            {
                'gas': 500000 + random.randint(1, 10000),
                'gasPrice': int(self.w3.eth.gas_price * 1.15),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            return True
        else:
            return False
        # logger.debug(f'HONEY转换STGUSDC成功,{transaction_receipt.status}')
        # return order_hash.hex()

    def bend_deposit(self, amount_in: int, amount_in_token_address: Union[Address]) -> bool:
        """
        bend deposit
        :param amount_in: 数量
        :param amount_in_token_address: 代币地址
        :return:
        """
        amount_in_token_contract = self.w3.eth.contract(address=amount_in_token_address, abi=erc_20_abi)
        token_balance = amount_in_token_contract.functions.balanceOf(self.account.address).call()
        assert token_balance != 0
        assert token_balance >= amount_in
        txn = self.bend_contract.functions.supply(asset=amount_in_token_address, amount=amount_in,
                                                  onBehalfOf=self.account.address, referralCode=0).build_transaction(
            {
                'gas': 500000 + random.randint(1, 10000),
                'gasPrice': int(self.w3.eth.gas_price * 1.15),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            return True
        else:
            return False

        # # logger.debug(f'存钱成功,{transaction_receipt.status}')
        # return order_hash.hex()

    def bend_borrow(self, amount_out: int, asset_token_address: Union[Address]) -> bool:
        """
        bend borrow
        :param amount_out: 数量
        :param asset_token_address: 借款代币地址
        :return:
        """
        txn = self.bend_contract.functions.borrow(asset=asset_token_address, amount=amount_out,
                                                  interestRateMode=2, referralCode=0,
                                                  onBehalfOf=self.account.address).build_transaction(
            {
                'gas': 500000 + random.randint(1, 10000),
                'gasPrice': int(self.w3.eth.gas_price * 1.15),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            return True
        else:
            return False
        # logger.debug(f'借款成功,{transaction_receipt.status}')
        # return order_hash.hex()

    def bend_repay(self, repay_amount: int, asset_token_address: Union[Address]) -> bool:
        """
        bend 还款
        :param repay_amount:还款数量
        :param asset_token_address: repay 代币地址
        :return:
        """
        txn = self.bend_contract.functions.repay(asset=asset_token_address, amount=repay_amount,
                                                 interestRateMode=2, onBehalfOf=self.account.address).build_transaction(
            {
                'gas': 500000 + random.randint(1, 10000), 'gasPrice': int(self.w3.eth.gas_price * 1.15),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            return True
        else:
            return False

    def honey_jar_mint(self):
        honey_balance = self.honey_contract.functions.balanceOf(self.account.address).call()
        has_mint = self.ooga_booga_contract.functions.hasMinted(self.account.address).call()
        if has_mint:
            # logger.debug(f'已mint！')
            return True
        signed_txn = self.w3.eth.account.sign_transaction(
            dict(
                chainId=80085,
                nonce=self.get_nonce(),
                gasPrice=int(self.w3.eth.gas_price * 1.15),
                gas=134500 + random.randint(1, 10000),
                to=self.w3.to_checksum_address(ooga_booga_address),
                data='0xa6f2ae3a',
            ),
            self.account.key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            # logger.debug(f'mint成功,{transaction_receipt.status}')
            return True
        else:
            # logger.debug(f'mint失败,{transaction_receipt.status}')
            return False

    def nft_mint(self):
        has_mint = self.nft_contract.functions.hasMinted(self.account.address).call()
        if has_mint:
            # logger.debug(f'已mint！')
            return True
        txn = self.nft_contract.functions.buy().build_transaction(
            {
                'gas': 500000 + random.randint(1, 10000), 'gasPrice': int(self.w3.eth.gas_price * 1.15),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            # logger.debug(f'mint成功,{transaction_receipt.status}')
            return True
        else:
            # logger.debug(f'mint失败,{transaction_receipt.status}')
            return False

    def nft2_mint(self):
        has_mint = self.nft2_contract.functions.hasMinted(self.account.address).call()
        if has_mint:
            # logger.debug(f'已mint！')
            return True
        txn = self.nft2_contract.functions.buy().build_transaction(
            {
                'gas': 500000 + random.randint(1, 10000), 'gasPrice': int(self.w3.eth.gas_price * 1.15),
                'nonce': self.get_nonce()
            })
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            # logger.debug(f'mint成功,{transaction_receipt.status}')
            return True
        else:
            # logger.debug(f'mint失败,{transaction_receipt.status}')
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
        set_solc_version(solc_version)
        compiled_sol = compile_source(contract_source_code)
        contract_id, contract_interface = compiled_sol.popitem()
        txn = dict(
            chainId=80085,
            gas=2000000,
            gasPrice=int(self.w3.eth.gas_price * 1.15),
            nonce=self.get_nonce(),
            data=contract_interface['bin'])
        signed_txn = self.w3.eth.account.sign_transaction(txn, private_key=self.private_key)
        order_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(order_hash)
        if transaction_receipt.status == 1:
            return True
        else:
            return False
