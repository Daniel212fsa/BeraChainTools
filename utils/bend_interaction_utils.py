import time
import random

from eth_account import Account
from loguru import logger

from bera_tools import BeraChainTools
from config.address_config import bend_address, weth_address, honey_address, bend_pool_address, weth_address, \
    honey_address


def bend_interacte(private_key, rpc_url, index):
    for _ in range(10):
        if bend_interacte_(private_key, rpc_url, index):
            break


def bend_interacte_(private_key, rpc_url, index):
    try:
        account = Account.from_key(private_key)
        bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
        logger.debug(f'第{index}次交互,开始存款')
        ahoney_balance = bera.ahoney_contract.functions.balanceOf(account.address).call()
        if ahoney_balance == 0:
            honey_balance = bera.honey_contract.functions.balanceOf(account.address).call()
            random_amount = round(random.uniform(0.10, 0.20), 2)
            approve_result = bera.approve_token(bend_address, honey_balance, honey_address)
            if approve_result:
                result = bera.bend_deposit(int(honey_balance * random_amount), honey_address)
                if result:
                    logger.success(f'第{index}次交互,honey存款成功,{result}')
                else:
                    logger.success(f'第{index}次交互,honey存款失败,{result}')
            else:
                logger.error(f'第{index}次交互,honey授权失败')
        else:
            logger.success(f'第{index}次交互,已存入honey')

        aweth_balance = bera.aweth_contract.functions.balanceOf(account.address).call()
        if aweth_balance == 0:
            weth_balance = bera.weth_contract.functions.balanceOf(account.address).call()
            random_amount = round(random.uniform(0.10, 0.20), 2)
            approve_result = bera.approve_token(bend_address, weth_balance, weth_address)
            if approve_result:
                result = bera.bend_deposit(int(weth_balance * random_amount), weth_address)
                if result:
                    logger.success(f'第{index}次交互,weth存款成功,{result}')
                else:
                    logger.success(f'第{index}次交互,weth存款失败,{result}')
            else:
                logger.error(f'第{index}次交互,weth授权失败')
        else:
            logger.success(f'第{index}次交互,已存入weth')

        # 已借贷的
        vdbalance = bera.vdhoney_contract.functions.balanceOf(account.address).call()
        # 可借贷的额度
        balance = bera.bend_contract.functions.getUserAccountData(account.address).call()[2]
        if vdbalance == 0:
            if balance > 0:
                logger.debug(f'第{index}次交互,可借{balance / 10 ** 8}')
                random_amount = round(random.uniform(0.10, 0.20), 2)
                result = bera.bend_borrow(int(balance * 10 ** 8 * random_amount), honey_address)
                if result:
                    logger.success(f'第{index}次交互,借款成功,{result}')
                else:
                    logger.error(f'第{index}次交互,借款失败,{result}')
            else:
                logger.error(f'第{index}次交互,借款失败,没有额度')
        else:
            logger.success(f'第{index}次交互,已经借过啦')

        vdbalance = bera.vdhoney_contract.functions.balanceOf(account.address).call()
        if vdbalance > 0:
            random_amount = round(random.uniform(0.10, 0.20), 2)
            result = bera.bend_repay(int(vdbalance * random_amount), honey_address)
            if result:
                logger.success(f'第{index}次交互,还款成功,{result}')
                return True
            else:
                logger.error(f'第{index}次交互,还款失败,{result}')
                return False
        else:
            logger.success(f'第{index}次交互,不用还款')
            return True
    except Exception as e:
        logger.error(f'第{index}次交互,{e}')
        # time.sleep(5)
        return False
