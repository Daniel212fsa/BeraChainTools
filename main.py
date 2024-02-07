import random
import os
import time
import configparser
from eth_account import Account
from loguru import logger

from utils.bend_interaction_utils import bend_interacte
from utils.bex_interaction_utils import bex_interacte
from utils.deploy_contract import deploy_contract
from utils.honey_interaction_utils import honey_interacte
from utils.honeyjar_interaction_utils import honeyjar_interacte
from utils.waters_utils import generate_wallet
from bera_tools import BeraChainTools
from utils.waters_utils import get_proxy
import concurrent.futures
from functools import partial


def interacte(arg):
    try:
        index, private_key, rpc_url, proxy_url, solver_provider, client_key, only_claim, on_action = arg
        account = Account.from_key(private_key)
        account_address = account.address
        logger.debug(f"第{index}次交互,地址:{account_address}")
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        has_mint = bera.ooga_booga_contract.functions.hasMinted(account.address).call()
        if has_mint:
            logger.debug(f"第{index}次交互,无需重复交互")
            return
        if not on_action:
            for i in range(10):
                balance = bera.get_balance()
                logger.debug(f"第{index}次交互,测试币余额 {balance / 10 ** 18}")
                if balance < 4 * 10 ** 16:
                    try:
                        result = bera.claim_bera(proxies=get_proxy(proxy_url))
                        if 'Txhash' in result.text or 'to the queue' in result.text:
                            logger.success(f'第{index}次交互,领水成功,{result.text}\n')
                            break
                        else:
                            logger.error(f'第{index}次交互,领水失败,{result.text}\n')
                    except Exception as e:
                        logger.error(f'第{index}次交互,领水失败,{e}\n')
                else:
                    break
        if only_claim:
            return
        balance = bera.get_balance()
        if balance > 0:
            bex_interacte(private_key, rpc_url, index)
            steps = [
                honey_interacte,
                honeyjar_interacte,
            ]
            random.shuffle(steps)
            for step in steps:
                step(private_key, rpc_url, index)
            steps = [
                bend_interacte,
                deploy_contract
            ]
            random.shuffle(steps)
            for step in steps:
                step(private_key, rpc_url, index)
    except Exception as e:
        logger.error(f'第{index}次交互,{e}')


if __name__ == '__main__':
    # 是否为初始化钱包模式
    mode_init_wallet = False
    # 只领水
    only_claim = False
    # 只交互
    on_action = True
    config = configparser.ConfigParser()
    config.read('config.ini')
    file_path = config.get('app', 'file_path')
    rpc_url = config.get('app', 'rpc_url')
    proxy_url = config.get('app', 'proxy_url')
    solver_provider = config.get('app', 'solver_provider')
    client_key = config.get('app', 'client_key')
    # 如果私钥文件,自动创建一个
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            file.write('')
    if mode_init_wallet:
        # 预期领水的地址数
        count = 1800
        # 线程数
        max_workers = 3
        generate_wallet(count, rpc_url, proxy_url, solver_provider, client_key, file_path, max_workers)
    else:
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
            args2.append([index, item[0], item[1], item[2], item[3], item[4], only_claim, on_action])
            index += 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # 将任务提交给线程池
            results = list(executor.map(interacte, args2))
