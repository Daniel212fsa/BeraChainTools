import random
import os
import time
import configparser
from eth_account import Account
from loguru import logger
from utils.create_domain import create_domain_nft
from utils.send_20 import send20
from utils.bend_interaction_utils import bend_interacte
from utils.bex_interaction_utils import bex_interacte
from utils.deploy_contract import deploy_contract
from utils.honetjar_nft_mint import nft_mint
from utils.honey_interaction_utils import honey_interacte
from utils.honeyjar_interaction_utils import honeyjar_interacte
from utils.waters_utils import generate_wallet
from bera_tools import BeraChainTools
# from utils.waters_utils import get_proxy
import concurrent.futures
from functools import partial
import random


def only_send20(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times, rpc_list = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        balance = bera.get_balance()
        if balance > 0:
            send20(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互失败,{account_address},没有测试币,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},领水失败,{e},耗时{time.time() - current_timestamp}')


def get_rand_rpc(rpc_url0, rpc_list0):
    if len(rpc_list0) > 0:
        return random.choice(rpc_list0.split(","))
    else:
        return rpc_url0


def only_create_domain_nft(arg):
    name = '创建域名'
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        logger.debug(f'第{index}次交互,{account_address},{name},rpc:{rpc_url}')
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        balance = bera.get_balance()
        if balance > 0:
            create_domain_nft(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},{name},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(
                f'第{index}次交互失败,{account_address},{name},没有测试币,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{name},{e},耗时{time.time() - current_timestamp}')


def only_claim(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        # logger.debug(f"第{index}次交互,地址:{account_address}")
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        for i in range(try_times):
            balance = bera.get_balance()
            logger.debug(f"第{index}次交互,{account_address},测试币余额 {balance / 10 ** 18}")
            if balance < 10 * 10 ** 16:
                try:
                    break
                    result = bera.claim_bera()
                    if 'Txhash' in result.text or 'to the queue' in result.text:
                        logger.success(
                            f'第{index}次交互,{account_address},领水成功,耗时{time.time() - current_timestamp},{result.text}\n')
                        break
                    else:
                        logger.error(
                            f'第{index}次交互,{account_address},领水失败,耗时{time.time() - current_timestamp},{result.text}\n')
                except Exception as e:
                    logger.error(
                        f'第{index}次交互,{account_address},领水失败,耗时{time.time() - current_timestamp},{e}\n')
            else:
                break
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},领水失败,{e},耗时{time.time() - current_timestamp}')


def only_mint(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
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
            nft_mint(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互失败,{account_address},没有测试币,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e},耗时{time.time() - current_timestamp}')


def claim_and_action(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        logger.debug(f"第{index}次交互,地址:{account_address}")
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        has_mint = bera.nft_contract.functions.hasMinted(account.address).call()
        if has_mint:
            logger.debug(f"第{index}次交互,{account_address},无需重复交互")
            return
        for i in range(try_times):
            balance = bera.get_balance()
            logger.debug(f"第{index}次交互,{account_address},测试币余额 {balance / 10 ** 18}")
            if balance < 4 * 10 ** 16:
                try:
                    result = bera.claim_bera()
                    if 'Txhash' in result.text or 'to the queue' in result.text:
                        logger.success(f'第{index}次交互,{account_address},领水成功,{result.text}\n')
                        break
                    else:
                        logger.error(f'第{index}次交互,{account_address},领水失败,{result.text}\n')
                except Exception as e:
                    logger.error(f'第{index}次交互,{account_address},领水失败,{e}\n')
            else:
                break
        balance = bera.get_balance()
        if balance > 0:
            bex_interacte(private_key, rpc_url, index, try_times)
            honey_interacte(private_key, rpc_url, index, try_times)
            steps = [
                honeyjar_interacte,
                bend_interacte,
                deploy_contract,
                nft_mint
            ]
            random.shuffle(steps)
            for step in steps:
                step(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互,{account_address},测试币不足,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e}')


def only_dex(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
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
            bex_interacte(private_key, rpc_url, index, try_times)
            honey_interacte(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互,{account_address},测试币不足,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e}')


def only_action(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        logger.debug(f"第{index}次交互,地址:{account_address}")
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        has_mint = bera.nft_contract.functions.hasMinted(account.address).call()
        if has_mint:
            logger.debug(f"第{index}次交互,{account_address},无需重复交互")
            return
        balance = bera.get_balance()
        if balance > 0:
            bex_interacte(private_key, rpc_url, index, try_times)
            honey_interacte(private_key, rpc_url, index, try_times)
            steps = [
                honeyjar_interacte,
                bend_interacte,
                deploy_contract,
                nft_mint
            ]
            random.shuffle(steps)
            for step in steps:
                step(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互,{account_address},测试币不足,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e}')


def get_app_item(values, index):
    if index in values:
        k = values[index]
    else:
        k = ''
    return k


if __name__ == '__main__':
    # 是否为初始化钱包模式
    mode_init_wallet = False
    try_times = 10
    config = configparser.ConfigParser()
    config.read('config.ini')
    app = config._sections['app']
    file_path = get_app_item(app, 'file_path')
    rpc_url = get_app_item(app, 'rpc_url')
    proxy_url = get_app_item(app, 'proxy_url')
    solver_provider = get_app_item(app, 'solver_provider')
    client_key = get_app_item(app, 'client_key')
    rpc_list = get_app_item(app, 'rpc_list')
    # print(file_path, rpc_url, proxy_url, solver_provider, client_key)
    # 如果私钥文件,自动创建一个
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            file.write('')
    if mode_init_wallet:
        # 预期领水的地址数
        count = 1800
        # 线程数
        max_workers = 5
        generate_wallet(count, get_rand_rpc(rpc_url, rpc_list), proxy_url, solver_provider, client_key, file_path,
                        max_workers)
    else:
        interaction_count = 0  # 初始化交互计数器
        args = []
        with open(file_path, 'r') as file:
            op = 0
            for private_key in file:
                private_key_str = private_key.strip()
                private_key_item = private_key_str.split(",")
                private_key_show = private_key_item[0]
                args.append([private_key_show, get_rand_rpc(rpc_url, rpc_list), proxy_url, solver_provider, client_key,
                             try_times])
                op += 1
                # break
        random.shuffle(args)
        args2 = []
        index = 0
        for item in args:
            args2.append([index, item[0], item[1], item[2], item[3], item[4], item[5]])
            index += 1
        modeList = [
            only_claim,  # 0
            only_mint,  # 1
            only_action,  # 2
            claim_and_action,  # 3
            only_send20,  # 4
            only_create_domain_nft,  # 5
            only_dex,  # 6
        ]
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # 将任务提交给线程池
            results = list(executor.map(modeList[5], args2))
