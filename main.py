import configparser
import random
import time

from eth_account import Account
from loguru import logger

from bera_tools import BeraChainTools
from utils.bend_interaction_utils import bend_interacte
from utils.bera_name_utils import mint_bera_name
from utils.bex_interaction_utils import bex_interacte
from utils.deploy_contract import deploy_contract
from utils.honetjar_nft_mint import nft_mint
from utils.honey_interaction_utils import honey_interacte
from utils.honeyjar_interaction_utils import honeyjar_interacte


def only_claim(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        logger.debug(f"第{index}次交互,地址:{account_address}")
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        for i in range(10):
            balance = bera.get_balance()
            logger.debug(f"第{index}次交互,测试币余额 {balance / 10 ** 18}")
            if balance < 4 * 10 ** 16:
                try:
                    pass
                    # result = bera.claim_bera(proxies=get_proxy(proxy_url))
                    # if 'Txhash' in result.text or 'to the queue' in result.text:
                    #     logger.success(
                    #         f'第{index}次交互,领水成功,耗时{time.time() - current_timestamp},{result.text}\n')
                    #     break
                    # else:
                    #     logger.error(f'第{index}次交互,领水失败,耗时{time.time() - current_timestamp},{result.text}\n')
                except Exception as e:
                    logger.error(f'第{index}次交互,领水失败,耗时{time.time() - current_timestamp},{e}\n')
            else:
                break
    except Exception as e:
        logger.error(f'第{index}次交互,领水失败,{e},耗时{time.time() - current_timestamp}')


def only_mint(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        logger.debug(f"第{index}次交互,地址:{account_address}")
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        balance = bera.get_balance()
        if balance > 0:
            nft_mint(private_key, rpc_url, index)
            logger.debug(f'第{index}次交互,交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互失败,没有测试币,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{e},耗时{time.time() - current_timestamp}')


def claim_and_action(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        logger.debug(f"第{index}次交互,地址:{account_address}")
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)

        balance = bera.get_balance()
        if balance > 0:
            bex_interacte(private_key, rpc_url, index)
            honey_interacte(private_key, rpc_url, index)
            steps = [
                honeyjar_interacte,
                bend_interacte,
                deploy_contract,
                nft_mint
            ]
            random.shuffle(steps)
            for step in steps:
                step(private_key, rpc_url, index)
            logger.debug(f'第{index}次交互,交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互,测试币不足,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{e}')


if __name__ == '__main__':
    # 是否为初始化钱包模式
    config = configparser.ConfigParser()
    file_path = './wallet/bera_private_keys.txt'
    rpc_url = 'https://rpc.ankr.com/berachain_testnet'
    proxy_url = ''
    solver_provider = ''
    client_key = ''

    interaction_count = 0  # 初始化交互计数器
    args = []
    with open(file_path, 'r') as file:
        for private_key in file:
            private_key_str = private_key.strip()
            private_key_item = private_key_str.split(",")
            private_key_show = private_key_item[0]
            args.append([private_key_show, rpc_url, proxy_url, solver_provider, client_key])
    random.shuffle(args)
    args2 = []
    index = 0
    for item in args:
        index += 1
        args2.append([index, item[0], item[1], item[2], item[3], item[4]])
    for args in args2:
        claim_and_action(args)
        print('\n\n')
