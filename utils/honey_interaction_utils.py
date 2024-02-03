import time
import random
from eth_account import Account
from loguru import logger

from bera_tools import BeraChainTools
from config.address_config import honey_swap_address, usdc_address, honey_address


def honey_interacte(private_key, rpc_url):
    for _ in range(10):
        if honey_interacte_(private_key, rpc_url):
            return


def honey_interacte_(private_key, rpc_url):
    account = Account.from_key(private_key)
    account_address = account.address
    bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)

    try:
        logger.debug(f'{account_address},STGUSDC转换HONEY开始')
        usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
        random_amount = round(random.uniform(0.70, 0.90), 2)
        amount = int(usdc_balance * random_amount)
        approve_result = bera.approve_token(honey_swap_address, amount, usdc_address)
        if approve_result:
            result = bera.honey_mint(amount)
            if result:
                logger.success(f'{account_address},STGUSDC转换HONEY成功,{result}')
            else:
                logger.error(f'{account_address},STGUSDC转换HONEY失败')
        else:
            logger.error(f'{account_address},STGUSDC转换HONEY失败')

        logger.debug(f'{account_address},HONEY转换STGUSDC开始')

        honey_balance = bera.honey_contract.functions.balanceOf(account.address).call()
        random_amount = round(random.uniform(0.01, 0.20), 2)
        amount = int(honey_balance * random_amount)
        approve_result = bera.approve_token(honey_swap_address, amount, honey_address)
        if approve_result:
            result = bera.honey_redeem(int(honey_balance * random_amount))
            if result:
                logger.success(f'{account_address},HONEY转换STGUSDC成功,{result}')
            else:
                logger.error(f'{account_address},HONEY转换STGUSDC失败')
        else:
            logger.error(f'{account_address},HONEY转换STGUSDC失败')

        logger.debug('-------------------------------------------------------------------------------------')
        return True
    except Exception as e:
        logger.error(e)
        return False
