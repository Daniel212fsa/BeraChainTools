from eth_account import Account
from loguru import logger
from bera_tools import BeraChainTools


def create_domain_nft(private_key, rpc_url, index, try_times):
    for _ in range(try_times):
        if create_domain_nft_(private_key, rpc_url, index):
            break


def create_domain_nft_(private_key, rpc_url, index):
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
        balance = bera.domain_contract.functions.balanceOf(account.address).call()
        if balance > 0:
            logger.success(f'第{index}次交互:{account_address},不用重复创建域名')
            return True
        # 部署合约
        result = bera.create_domain()
        if result:
            logger.success(f'第{index}次交互:{account_address},创建域名成功,{result}')
            logger.debug('-------------------------------------------------------------------------------------')
            return True
        else:
            logger.error(f'第{index}次交互:{account_address},创建域名失败,{result}')
            return False
    except Exception as e:
        logger.error(f'第{index}次交互:{account_address},创建域名失败，{e}')
        return False
