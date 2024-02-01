from eth_account import Account
from loguru import logger
import random
from bera_tools import BeraChainTools
from config.address_config import (
    usdc_address, wbear_address, weth_address, bex_approve_liquidity_address,
    usdc_pool_liquidity_address, weth_pool_liquidity_address
)


def swap_usdc(account, bera):
    for i in range(10):
        try:
            # bex 使用bera交换usdc
            bera_balance = bera.w3.eth.get_balance(account.address)
            usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
            if usdc_balance > 0:
                logger.success("已兑换过usdc!")
                break
            logger.debug(f'usdc_balance,{usdc_balance / 10 ** 18}')
            random_amount = round(random.uniform(0.10, 0.20), 2)
            result = bera.bex_swap(int(bera_balance * random_amount), wbear_address, usdc_address)
            usdc_balance_new = bera.usdc_contract.functions.balanceOf(account.address).call()
            logger.debug(f'usdc_balance:{usdc_balance / 10 ** 18},usdc_balance_new:{usdc_balance_new / 10 ** 18}')
            if result:
                logger.success(f'bex 使用bera交换usdc成功,{result}')
                break
            else:
                logger.error(f'bex 使用bera交换usdc失败,{result}')
        except Exception as e:
            logger.error(f'bex 使用bera交换usdc失败,{e}')


def swap_weth(account, bera):
    for j in range(10):
        try:
            # bex 使用bera交换weth
            bera_balance = bera.w3.eth.get_balance(account.address)
            weth_balance = bera.weth_contract.functions.balanceOf(account.address).call()
            if weth_balance > 0:
                logger.success("已兑换过weth!")
                break
            logger.debug(f'weth_balance:{weth_balance}')
            random_amount = round(random.uniform(0.10, 0.20), 2)
            result = bera.bex_swap(int(bera_balance * random_amount), wbear_address, weth_address)
            weth_balance_new = bera.weth_contract.functions.balanceOf(account.address).call()
            logger.debug(f'weth_balance:{weth_balance / 10 ** 18},weth_balance_new:{weth_balance_new / 10 ** 18}')
            if result:
                logger.success(f'bex 使用bera交换weth成功,{result}')
                break
            else:
                logger.error(f'bex 使用bera交换weth失败,{result}')
        except Exception as e:
            logger.error(f'bex 使用bera交换weth失败,{e}')


def add_liquidity_usdc(account, bera):
    for m in range(10):
        try:
            usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
            if usdc_balance == 0:
                logger.error(f'没有usdc,自动跳过!')
                break
            approve_result = bera.approve_token(bex_approve_liquidity_address, usdc_balance, usdc_address)
            if approve_result:
                logger.success(f'授权成功!')
                for k in range(10):
                    try:
                        random_amount = round(random.uniform(0.10, 0.20), 2)
                        result = bera.bex_add_liquidity(int(usdc_balance * random_amount), usdc_pool_liquidity_address,
                                                        usdc_address)
                        if result:
                            logger.success(f'增加 usdc 流动性成功,{result}')
                            break
                        else:
                            logger.error(f'增加 usdc 流动性失败,{result}')
                    except Exception as e:
                        logger.error(f'增加 usdc 流动性失败,{e}')
                break
            else:
                logger.error(f'授权失败!')
        except Exception as e:
            logger.error(f'增加 usdc 流动性失败,{e}')


def add_liquidity_weth(account, bera):
    for k in range(10):
        try:
            weth_balance = bera.weth_contract.functions.balanceOf(account.address).call()
            if weth_balance == 0:
                logger.error(f'没有weth,自动跳过!')
                break
            approve_result = bera.approve_token(bex_approve_liquidity_address, weth_balance, weth_address)
            if approve_result:
                logger.success(f'授权成功!')
                for t in range(10):
                    try:
                        random_amount = round(random.uniform(0.10, 0.20), 2)
                        result = bera.bex_add_liquidity(int(weth_balance * random_amount), weth_pool_liquidity_address,
                                                        weth_address)
                        if result:
                            logger.success(f'增加 weth 流动性成功,{result}')
                            break
                        else:
                            logger.error(f'增加 weth 流动性失败！！！,{result}')
                    except Exception as e:
                        logger.error(f'增加 weth 流动性失败！！！,{e}')
                break
            else:
                logger.error(f'授权失败!')
        except Exception as e:
            logger.error(f'增加 weth 流动性失败！！！,{e}')


def bex_interacte(private_key, rpc_url):
    logger.debug('开始Bex 交互')

    account = Account.from_key(private_key)
    bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
    random_number = random.randint(1, 6)
    if random_number == 1:
        swap_usdc(account, bera)
        swap_weth(account, bera)
        add_liquidity_usdc(account, bera)
        add_liquidity_weth(account, bera)
    elif random_number == 2:
        swap_usdc(account, bera)
        swap_weth(account, bera)
        add_liquidity_weth(account, bera)
        add_liquidity_usdc(account, bera)
    elif random_number == 3:
        swap_weth(account, bera)
        swap_usdc(account, bera)
        add_liquidity_usdc(account, bera)
        add_liquidity_weth(account, bera)
    elif random_number == 4:
        swap_weth(account, bera)
        swap_usdc(account, bera)
        add_liquidity_weth(account, bera)
        add_liquidity_usdc(account, bera)
    elif random_number == 5:
        swap_usdc(account, bera)
        add_liquidity_usdc(account, bera)
        swap_weth(account, bera)
        add_liquidity_weth(account, bera)
    elif random_number == 6:
        swap_weth(account, bera)
        add_liquidity_weth(account, bera)
        swap_usdc(account, bera)
        add_liquidity_usdc(account, bera)

    logger.success('Bex 交互结束')
    logger.debug('-------------------------------------------------------------------------------------')
