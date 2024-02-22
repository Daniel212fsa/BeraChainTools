import time
import random
from eth_account import Account
from loguru import logger

from bera_tools import BeraChainTools
from config.address_config import ooga_booga_address, honey_address, wbear_address, usdc_address, nft_address, \
    nft2_address


# ooga_booga_address  4.2honey
# nft_address
# nft2_address 2.22 honey
def nft_mint(private_key, rpc_url, index, try_times):
    account = Account.from_key(private_key)
    account_address = account.address
    bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
    total_swap_amount = 0
    # has_mint_nft2 = bera.nft2_contract.functions.hasMinted(account.address).call()
    # if not has_mint_nft2:
    #     total_swap_amount += 2.22 * 10 ** 18
    has_mint_oga = bera.ooga_booga_contract.functions.hasMinted(account.address).call()
    if not has_mint_oga:
        total_swap_amount += 4.2 * 10 ** 18
    for i in range(try_times):
        honey_balance = bera.honey_contract.functions.balanceOf(account.address).call()
        if honey_balance < total_swap_amount:
            swap_amount = int(total_swap_amount - honey_balance + 1 * 10 ** 18)
            usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
            if usdc_balance < swap_amount:
                bera_balance = bera.w3.eth.get_balance(account.address)
                random_amount = round(random.uniform(0.20, 0.25), 2)
                bera.bex_swap(int(bera_balance * random_amount), wbear_address, usdc_address)
                bera.honey_mint(swap_amount)
            else:
                bera.honey_mint(swap_amount)
        else:
            break
    # exit()
    # if not has_mint_nft2:
    #     for _ in range(try_times):
    #         if nft_mint_(private_key, rpc_url, index, try_times, bera, bera.nft2_contract, nft2_address, bera.nft2_mint,
    #                      222 * 10 ** 16, 'nft2'):
    #             break
    if not has_mint_oga:
        for _ in range(try_times):
            if nft_mint_(private_key, rpc_url, index, try_times, bera, bera.ooga_booga_contract, ooga_booga_address,
                         bera.honey_jar_mint,
                         420 * 10 ** 16, 'ooga_booga'):
                break


def nft_mint_(private_key, rpc_url, index, try_times, bera, nft_contract, nft_contract_address, action, price, name):
    account = Account.from_key(private_key)
    account_address = account.address
    try:
        logger.debug(f'第{index}次交互:{account_address},{name} mint 交互开始')
        # has_mint = nft_contract.functions.hasMinted(account.address).call()
        # if has_mint:
        #     logger.success(f'第{index}次交互:{account_address},之前mint过了{nft_contract_address},{name} mint 交互成功')
        #     logger.debug('-------------------------------------------------------------------------------------')
        #     return True
        # usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
        # honey_balance = bera.honey_contract.functions.balanceOf(account.address).call()
        # logger.debug(
        #     f'第{index}次交互:{account_address},usdc_balance:{usdc_balance / 10 ** 18},honey_balance:{honey_balance / 10 ** 18},价格：{price / 10 ** 18}')
        approve_result = bera.approve_token(nft_contract_address, 5 * 10 ** 18, honey_address)
        if approve_result:
            # if honey_balance < price:
            #     for i in range(try_times):
            #         swap_amount = int(total_price - honey_balance)
            #         usdc_balance = bera.usdc_contract.functions.balanceOf(account.address).call()
            #         if usdc_balance < swap_amount:
            #             bera_balance = bera.w3.eth.get_balance(account.address)
            #             random_amount = round(random.uniform(0.20, 0.25), 2)
            #             bera.bex_swap(int(bera_balance * random_amount), wbear_address, usdc_address)
            #             bera.honey_mint(swap_amount)
            #         else:
            #             bera.honey_mint(swap_amount)
            #         honey_balance = bera.honey_contract.functions.balanceOf(account.address).call()
            #         if honey_balance >= price:
            #             break
            # else:
            #     logger.success(f'第{index}次交互:{account_address},无须兑换,直接mint {name}')

            result = action()
            if result:
                logger.success(f'第{index}次交互:{account_address},{name} mint 交互成功,{result}')
                logger.debug('-------------------------------------------------------------------------------------')
                return True
            else:
                return False
        else:
            logger.error(f'第{index}次交互:{account_address},{name} mint 交互失败,授权失败')
            return False
    except Exception as e:
        logger.error(f'第{index}次交互:{account_address},{name} mint 交互失败,{e}')
        # time.sleep(5)
        return False
