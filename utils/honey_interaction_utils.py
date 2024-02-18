import time
import random
from eth_account import Account
from loguru import logger

from bera_tools import BeraChainTools
from config.address_config import honey_swap_address, usdc_address, honey_address


def honey_interacte(private_key, rpc_url, index, try_times):
    for _ in range(try_times):
        if honey_interacte_1(private_key, rpc_url, index, try_times):
            break
    for _ in range(try_times):
        if honey_interacte_2(private_key, rpc_url, index, try_times):
            break


def honey_interacte_1(private_key, rpc_url, index, try_times):
    account = Account.from_key(private_key)
    account_address = account.address
    bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
    honey_balance = bera.honey_contract.functions.balanceOf(account.address).call()
    if honey_balance > 0:
        if honey_balance > 0:
            logger.debug(f'第{index}次交互:{account_address},HONEY转换STGUSDC,无需重复')
            return True
    try:
        logger.debug(f'第{index}次交互:{account_address},STGUSDC转换HONEY开始')
        usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
        random_amount = round(random.uniform(0.80, 0.90), 2)
        amount = int(usdc_balance * random_amount)
        approve_result = bera.approve_token(honey_swap_address, amount, usdc_address)
        if approve_result:
            result = bera.honey_mint(amount)
            if result:
                logger.success(f'第{index}次交互:{account_address},STGUSDC转换HONEY成功,{result}')
                return True
            else:
                logger.error(f'第{index}次交互:{account_address},STGUSDC转换HONEY失败')
                return False
        else:
            logger.error(f'第{index}次交互:{account_address},授权失败')
            return False
    except Exception as e:
        logger.error(f'第{index}次交互:{account_address},{e}')
        return False


def honey_interacte_2(private_key, rpc_url, index, try_times):
    account = Account.from_key(private_key)
    account_address = account.address
    bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
    honey_balance = bera.honey_contract.functions.balanceOf(account.address).call()
    if honey_balance > 0:
        logger.debug(f'第{index}次交互:{account_address},HONEY转换STGUSDC,无需重复')
        return True
    try:
        logger.debug(f'第{index}次交互:{account_address},HONEY转换STGUSDC开始')
        honey_balance = bera.honey_contract.functions.balanceOf(account.address).call()
        random_amount = round(random.uniform(0.01, 0.10), 2)
        amount = int(honey_balance * random_amount)
        approve_result = bera.approve_token(honey_swap_address, amount, honey_address)
        if approve_result:
            result = bera.honey_redeem(int(honey_balance * random_amount))
            if result:
                logger.success(f'第{index}次交互:{account_address},HONEY转换STGUSDC成功,{result}')
                logger.debug('-------------------------------------------------------------------------------------')
                return True
            else:
                logger.error(f'第{index}次交互:{account_address},HONEY转换STGUSDC失败')
                return False
        else:
            logger.error(f'第{index}次交互:{account_address},授权失败')
            return False
    except Exception as e:
        logger.error(f'第{index}次交互:{account_address},{e}')
        return False
