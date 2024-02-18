from eth_account import Account
from loguru import logger
from bera_tools import BeraChainTools


def send20(private_key, rpc_url, index, try_times):
    for _ in range(try_times):
        if send20_(private_key, rpc_url, index):
            break


def send20_(private_key, rpc_url, index):
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        bera = BeraChainTools(private_key=account.key, rpc_url=rpc_url)

        # 部署合约
        result = bera.send_bera20()
        if result:
            logger.success(f'第{index}次交互:{account_address},发送铭文成功,{result}')
            logger.debug('-------------------------------------------------------------------------------------')
            return True
        else:
            logger.error(f'第{index}次交互:{account_address},发送铭文失败,{result}')
            return False
    except Exception as e:
        logger.error(f'第{index}次交互:{account_address},发送铭文失败，{e}')
        return False
