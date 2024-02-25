import requests
import json
from eth_account import Account
from loguru import logger
import random
from bera_tools import BeraChainTools
from config.address_config import (
    usdc_address, wbear_address, weth_address, bex_approve_liquidity_address,
    usdc_pool_liquidity_address, weth_pool_liquidity_address
)


def add_liquidity_usdc(account, bera, index, try_times):
    account_address = account.address
    url = 'https://api.goldsky.com/api/public/project_clqy1ct1fqf18010n972w2xg7/subgraphs/dex-test/v0.0.1/gn'
    user_agent = bera.fake.chrome()
    headers = {
        'authority': "api.goldsky.com",
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://artio.faucet.berachain.com',
        'pragma': 'no-cache',
        'referer': 'https://artio.faucet.berachain.com/',
        'user-agent': user_agent
    }
    for m in range(try_times):
        try:
            params = {"operationName": "GetUserPools", "variables": {"userAddress": account_address},
                      "query": "query GetUserPools($userAddress: String!) {\n  userPools(where: {userAddress: $userAddress}) {\n    id\n    poolAddress\n    shares\n    userAddress\n    __typename\n  }\n}"}
            response = requests.post(
                url,
                # params=params,
                headers=headers,
                data=json.dumps(params),
                timeout=30
            )
            if usdc_pool_liquidity_address.lower() in response.text:
                logger.success(f'第{index}次交互:{account_address},已添加weth流动性')
                break
            usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
            if usdc_balance == 0:
                logger.error(f'第{index}次交互:{account_address},没有usdc,自动跳过!')
                break
            approve_result = bera.approve_token(bex_approve_liquidity_address, usdc_balance, usdc_address)
            if approve_result:
                logger.success(f'第{index}次交互:{account_address},授权成功!')
                for k in range(try_times):
                    try:
                        random_amount = round(random.uniform(0.05, 0.10), 2)
                        result = bera.bex_add_liquidity(int(usdc_balance * random_amount), usdc_pool_liquidity_address,
                                                        usdc_address)
                        if result:
                            logger.success(f'第{index}次交互:{account_address},增加 usdc 流动性成功,{result}')
                            break
                        else:
                            logger.error(f'第{index}次交互:{account_address},增加 usdc 流动性失败,{result}')
                    except Exception as e:
                        logger.error(f'第{index}次交互:{account_address},增加 usdc 流动性失败,{e}')
                break
            else:
                logger.error(f'第{index}次交互:{account_address},授权失败!')
        except Exception as e:
            logger.error(f'第{index}次交互:{account_address},增加 usdc 流动性失败,{e}')


def add_liquidity_weth(account, bera, index, try_times):
    account_address = account.address
    url = 'https://api.goldsky.com/api/public/project_clqy1ct1fqf18010n972w2xg7/subgraphs/dex-test/v0.0.1/gn'
    user_agent = bera.fake.chrome()
    headers = {
        'authority': "api.goldsky.com",
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://artio.faucet.berachain.com',
        'pragma': 'no-cache',
        'referer': 'https://artio.faucet.berachain.com/',
        'user-agent': user_agent
    }

    for k in range(try_times):
        try:
            params = {"operationName": "GetUserPools", "variables": {"userAddress": account_address},
                      "query": "query GetUserPools($userAddress: String!) {\n  userPools(where: {userAddress: $userAddress}) {\n    id\n    poolAddress\n    shares\n    userAddress\n    __typename\n  }\n}"}
            response = requests.post(
                url,
                # params=params,
                headers=headers,
                data=json.dumps(params),
                timeout=30
            )
            if weth_pool_liquidity_address.lower() in response.text:
                logger.success(f'第{index}次交互:{account_address},已添加weth流动性')
                break
            weth_balance = bera.weth_contract.functions.balanceOf(account.address).call()
            if weth_balance == 0:
                logger.error(f'第{index}次交互:{account_address},没有weth,自动跳过!')
                break
            approve_result = bera.approve_token(bex_approve_liquidity_address, weth_balance, weth_address)
            if approve_result:
                logger.success(f'第{index}次交互:{account_address},授权成功!')
                for t in range(try_times):
                    try:
                        random_amount = round(random.uniform(0.20, 0.30), 2)
                        result = bera.bex_add_liquidity(int(weth_balance * random_amount), weth_pool_liquidity_address,
                                                        weth_address)
                        if result:
                            logger.success(f'第{index}次交互:{account_address},增加 weth 流动性成功,{result}')
                            break
                        else:
                            logger.error(f'第{index}次交互:{account_address},增加 weth 流动性失败！！！,{result}')
                    except Exception as e:
                        logger.error(f'第{index}次交互:{account_address},增加 weth 流动性失败！！！,{e}')
                break
            else:
                logger.error(f'第{index}次交互:{account_address},授权失败!')
        except Exception as e:
            logger.error(f'第{index}次交互:{account_address},增加 weth 流动性失败！！！,{e}')


def bex_liquidity(private_key, rpc_url, index, try_times):
    account = Account.from_key(private_key)
    account_address = account.address
    logger.debug(f'第{index}次交互:{account_address},开始Bex 交互--添加流动性')
    bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
    random_number = random.randint(1, 2)
    if random_number == 1:
        add_liquidity_usdc(account, bera, index, try_times)
        add_liquidity_weth(account, bera, index, try_times)
    elif random_number == 2:
        add_liquidity_weth(account, bera, index, try_times)
        add_liquidity_usdc(account, bera, index, try_times)
    logger.success(f'第{index}次交互:{account_address},Bex 交互 添加流动性 结束')
    logger.debug('-------------------------------------------------------------------------------------')
