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


def swap_usdc(account, bera, index, try_times):
    account_address = account.address
    for i in range(try_times):
        try:
            # bex 使用bera交换usdc
            bera_balance = bera.w3.eth.get_balance(account.address)
            usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
            if usdc_balance > 0:
                logger.success(f"第{index}次交互:{account_address},已兑换过usdc!")
                break
            logger.debug(f'{account_address},usdc_balance,{usdc_balance / 10 ** 18}')
            random_amount = round(random.uniform(0.20, 0.25), 2)
            result = bera.bex_swap(int(bera_balance * random_amount), wbear_address, usdc_address)
            usdc_balance_new = bera.usdc_contract.functions.balanceOf(account.address).call()
            logger.debug(
                f'第{index}次交互:{account_address},usdc_balance:{usdc_balance / 10 ** 18},usdc_balance_new:{usdc_balance_new / 10 ** 18}')
            if result:
                logger.success(f'第{index}次交互:{account_address},使用bera交换usdc成功,{result}')
                break
            else:
                logger.error(f'第{index}次交互:{account_address},使用bera交换usdc失败,{result}')
        except Exception as e:
            logger.error(f'第{index}次交互:{account_address},使用bera交换usdc失败,{e}')


def swap_weth(account, bera, index, try_times):
    account_address = account.address
    for j in range(try_times):
        try:
            # bex 使用bera交换weth
            bera_balance = bera.w3.eth.get_balance(account.address)
            weth_balance = bera.weth_contract.functions.balanceOf(account.address).call()
            if weth_balance > 0:
                logger.success(f"第{index}次交互:{account_address},已兑换过weth!")
                break
            logger.debug(f'第{index}次交互:{account_address},weth_balance:{weth_balance}')
            random_amount = round(random.uniform(0.05, 0.10), 2)
            result = bera.bex_swap(int(bera_balance * random_amount), wbear_address, weth_address)
            weth_balance_new = bera.weth_contract.functions.balanceOf(account.address).call()
            logger.debug(
                f'第{index}次交互:{account_address},weth_balance:{weth_balance / 10 ** 18},weth_balance_new:{weth_balance_new / 10 ** 18}')
            if result:
                logger.success(f'第{index}次交互:{account_address},bex 使用bera交换weth成功,{result}')
                break
            else:
                logger.error(f'第{index}次交互:{account_address},bex 使用bera交换weth失败,{result}')
        except Exception as e:
            logger.error(f'第{index}次交互:{account_address},bex 使用bera交换weth失败,{e}')


def bex_swap(private_key, rpc_url, index, try_times):
    account = Account.from_key(private_key)
    account_address = account.address
    logger.debug(f'第{index}次交互:{account_address},开始Bex 交互')
    bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
    random_number = random.randint(1, 2)
    if random_number == 1:
        swap_usdc(account, bera, index, try_times)
        swap_weth(account, bera, index, try_times)
    elif random_number == 2:
        swap_weth(account, bera, index, try_times)
        swap_usdc(account, bera, index, try_times)
    logger.success(f'第{index}次交互:{account_address},Bex 交互结束')
    logger.debug('-------------------------------------------------------------------------------------')
