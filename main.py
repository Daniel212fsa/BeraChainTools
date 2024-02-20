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
# from utils.honeyjar_interaction_utils import honeyjar_interacte
# from utils.waters_utils import generate_wallet
from bera_tools import BeraChainTools
# from utils.waters_utils import get_proxy
import concurrent.futures
# from functools import partial
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
        logger.debug(f'第{index}次交互,{account_address},{name},rpc: {rpc_url}')
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
                    # break
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


def only_bend(arg):
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
            bend_interacte(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互失败,{account_address},没有测试币,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e},耗时{time.time() - current_timestamp}')


def only_deploy_contract(arg):
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
            deploy_contract(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互失败,{account_address},没有测试币,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e},耗时{time.time() - current_timestamp}')


def only_dex(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        logger.debug(f"第{index}次交互,地址:{account_address},rpc: {rpc_url}")
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        balance = bera.get_balance()
        if balance > 0:
            bex_interacte(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互,{account_address},测试币不足,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e}')


def only_honey(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        logger.debug(f"第{index}次交互,地址:{account_address},rpc: {rpc_url}")
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        balance = bera.get_balance()
        if balance > 0:
            honey_interacte(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互,{account_address},测试币不足,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e}')


def only_send20_create_domain_nft_deploy_contract_bend(arg):
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
            steps = [
                send20,
                create_domain_nft,
                deploy_contract,
                bend_interacte
            ]
            random.shuffle(steps)
            for step in steps:
                step(private_key, rpc_url, index, try_times)
            logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')
        else:
            logger.error(f'第{index}次交互,{account_address},测试币不足,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e}')


def all_action(arg):
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
            nft_mint(private_key, rpc_url, index, try_times)
            steps = [
                send20,
                create_domain_nft,
                deploy_contract,
                bend_interacte
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


def main(try_times, max_workers, mode_index):
    # try_times = 10
    config = configparser.ConfigParser()
    config.read('config.ini')
    app = config._sections['app']
    file_path = get_app_item(app, 'file_path')
    rpc_url = get_app_item(app, 'rpc_url')
    proxy_url = get_app_item(app, 'proxy_url')
    solver_provider = get_app_item(app, 'solver_provider')
    client_key = get_app_item(app, 'client_key')
    rpc_list = get_app_item(app, 'rpc_list')
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
    # 流程：领水->交互DEX->UDSC兑换Honey->mint三张NFT/域名交互/发送铭文/借贷交互/部署合约
    mode_list = [
        only_claim,  # 0 只领水
        only_dex,  # 1 只兑换
        only_honey,  # 2 只交换Hoeny和USDC
        only_mint,  # 3 只mintNFT,要有足够的Honey
        only_send20,  # 4 只发送铭文
        only_create_domain_nft,  # 5 只交互域名
        only_deploy_contract,  # 6 只部署合约
        only_bend,  # 7 只借贷
        only_send20_create_domain_nft_deploy_contract_bend,  # 8 混合任务
        all_action,  # 9 完成所有交互任务
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 将任务提交给线程池
        results = list(executor.map(mode_list[mode_index], args2))


if __name__ == '__main__':
    only_claim_mode = False  # 只批量领水
    only_action_mode = True  # 只批量交互
    for i in range(3):
        if only_claim_mode and not only_action_mode:
            main(5, 5, 0)  # 领水
            break
        # main(5, 5, 1)  # 只兑换
        # main(5, 5, 2)  # 只交换Hoeny和USDC
        # main(5, 5, 3)  # 只mintNFT,要有足够的Honey
        # main(5, 5, 8)  # 只发送铭文/只交互域名/只部署合约/只借贷

        main(5, 10, 9)
