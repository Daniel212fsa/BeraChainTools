import time
import random
from eth_account import Account
from loguru import logger

from bera_tools import BeraChainTools
from config.address_config import ooga_booga_address, honey_address, wbear_address, usdc_address


# from config.address_config import bex_swap_address, usdc_address, honey_address, honey_swap_address, \
#     bex_approve_liquidity_address, weth_address, bend_address, bend_borrows_address, wbear_address, zero_address, \
#     ooga_booga_address
def honeyjar_interacte(private_key, rpc_url, index):
    for _ in range(10):
        if honeyjar_interacte_(private_key, rpc_url, index):
            return


def honeyjar_interacte_(private_key, rpc_url, index):
    account = Account.from_key(private_key)
    account_address = account.address
    try:
        logger.debug(f'第{index}次交互:{account_address},0xhoneyjar 交互开始')
        bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
        bera_balance = bera.w3.eth.get_balance(account.address)
        has_mint = bera.ooga_booga_contract.functions.hasMinted(account.address).call()
        if has_mint:
            logger.success(f'第{index}次交互:{account_address},之前mint过了,0xhoneyjar 交互成功')
            logger.debug('-------------------------------------------------------------------------------------')
            return True
        # 如果usdc余额不足,先兑换udsc
        usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
        if usdc_balance < 42 * 10 ** 17:
            for i in range(10):
                random_amount = round(random.uniform(0.10, 0.20), 2)
                result = bera.bex_swap(int(bera_balance * random_amount), wbear_address, usdc_address)
                if result:
                    break

        honey_balance = bera.honey_contract.functions.balanceOf(account.address).call()
        logger.debug(
            f'第{index}次交互:{account_address},usdc_balance:{usdc_balance / 10 ** 18},honey_balance:{honey_balance / 10 ** 18}')
        approve_result = bera.approve_token(ooga_booga_address, 5 * 10 ** 18, honey_address)
        if approve_result:
            if honey_balance < 42 * 10 ** 17:
                for i in range(10):
                    random_amount = round(random.uniform(4.30, 6.20), 2)
                    result = bera.bex_swap(int(random_amount * 10 ** 18), usdc_address, honey_address)
                    if result:
                        break
            else:
                logger.success(f'第{index}次交互:{account_address},无须兑换,直接mint')

            result = bera.honey_jar_mint()
            if result:
                logger.success(f'第{index}次交互:{account_address},0xhoneyjar 交互成功,{result}')
                logger.debug('-------------------------------------------------------------------------------------')
                return True
            else:
                return False
        else:
            logger.error(f'第{index}次交互:{account_address},授权失败!')
            return False
    except Exception as e:
        logger.error(f'第{index}次交互:{account_address},0xhoneyjar 交互失败，{e}')
        # time.sleep(5)
        return False
