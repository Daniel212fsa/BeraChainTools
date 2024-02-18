from eth_account import Account
from loguru import logger

from bera_tools import BeraChainTools


def mint_bera_name(private_key, rpc_url, index):
    for _ in range(10):
        if mint_bera_name_(private_key, rpc_url, index):
            break


def mint_bera_name_(private_key, rpc_url, index):
    try:
        account = Account.from_key(private_key)
        bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)
        bera.create_bera_name()
        logger.success(f'第{index}次交互:注册Bera Name成功')
        return True
    except Exception as e:
        logger.error(f'第{index}次交互:注册Bera Name失败，{e}')
        return False