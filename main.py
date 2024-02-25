import random
import os
import time
import configparser
from eth_account import Account
from loguru import logger
from utils.create_domain import create_domain_nft
from utils.send_20 import send20
from utils.bend_interaction_utils import bend_interacte
from utils.bex_liquidity_utils import bex_liquidity
from utils.bex_swap_utils import bex_swap
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
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
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


def only_check_gas(arg):
    current_timestamp = time.time()
    index, private_key, rpc_url, proxy_url, solver_provider, client_key, try_times = arg
    try:
        account = Account.from_key(private_key)
        account_address = account.address
        bera = BeraChainTools(private_key=private_key,
                              proxy_url=proxy_url,
                              client_key=client_key,
                              solver_provider=solver_provider,
                              rpc_url=rpc_url)
        balance = bera.get_balance()
        logger.debug(
            f"第{index}次交互,地址: {account_address},测试币余额: {balance / 10 ** 18},耗时{time.time() - current_timestamp}")

    except Exception as e:
        logger.error(f'第{index}次交互,地址: {account_address},检测余额失败,耗时{time.time() - current_timestamp}')


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
            bex_swap(private_key, rpc_url, index, try_times)
            bex_liquidity(private_key, rpc_url, index, try_times)
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


def append_data(data):
    file_path = 'wallet/bera_private_keys_hcy_auto_all_ok.txt'
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            pass
    with open(file_path, "r") as file:
        lines = file.readlines()
    if data + "\n" not in lines:
        with open(file_path, "a") as file:
            file.write(data + "\n")
    else:
        print("数据已存在，不进行追加操作")


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
        gas_price = bera.get_gas_price()
        # config = configparser.ConfigParser()
        # config.read('config.ini')
        # app = config._sections['app']
        # max_gas_price = get_app_item(app, 'max_gas_price')
        # if max_gas_price == '':
        max_gas_price = 10 ** 10
        if gas_price < int(max_gas_price):
            logger.debug(f'第{index}次交互,{account_address},当前gas: {gas_price / 10 ** 9}')
            balance = bera.get_balance()
            if balance > 0:
                has_mint_oga = bera.ooga_booga_contract.functions.hasMinted(account_address).call()
                ahoney_balance = bera.ahoney_contract.functions.balanceOf(account.address).call()
                domain_balance = bera.domain_contract.functions.balanceOf(account.address).call()
                if has_mint_oga and ahoney_balance > 0 and domain_balance > 0:
                    append_data(private_key + ',,' + account_address)
                    logger.success(
                        f'第{index}次交互,{account_address},已经交互过了,耗时{time.time() - current_timestamp}')
                else:
                    steps_lsit = [
                        [
                            [
                                bex_swap,
                                create_domain_nft,
                                deploy_contract
                            ],
                            [
                                bex_liquidity,
                                honey_interacte
                            ],
                            [
                                nft_mint,
                                bend_interacte
                            ]
                        ],
                        [
                            [
                                bex_swap,
                            ],
                            [
                                create_domain_nft,
                                deploy_contract,
                                bex_liquidity,
                                honey_interacte
                            ],
                            [
                                nft_mint,
                                bend_interacte
                            ]
                        ],
                        [
                            [
                                bex_swap
                            ],
                            [
                                bex_liquidity,
                                honey_interacte
                            ],
                            [
                                nft_mint,
                                bend_interacte,
                                create_domain_nft,
                                deploy_contract
                            ]
                        ],
                    ]
                    steps_lsit_new = random.choice(steps_lsit)
                    for step_item in steps_lsit_new:
                        random.shuffle(step_item)
                        for step in step_item:
                            step(private_key, rpc_url, index, try_times)
                    has_mint_oga = bera.ooga_booga_contract.functions.hasMinted(account_address).call()
                    ahoney_balance = bera.ahoney_contract.functions.balanceOf(account.address).call()
                    domain_balance = bera.domain_contract.functions.balanceOf(account.address).call()
                    if has_mint_oga and ahoney_balance > 0 and domain_balance > 0:
                        append_data(private_key + ',,' + account_address)
                        logger.success(
                            f'第{index}次交互,{account_address},已经交互过了,耗时{time.time() - current_timestamp}')
                    logger.debug(f'第{index}次交互,{account_address},交互结束,耗时{time.time() - current_timestamp}')

            else:
                logger.error(f'第{index}次交互,{account_address},测试币不足,耗时{time.time() - current_timestamp}')
        else:
            logger.debug(f'第{index}次交互,{account_address},当前gas: {gas_price / 10 ** 9}')
            logger.error(f'第{index}次交互,{account_address},gasPrice过高,耗时{time.time() - current_timestamp}')
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e}')


def check_all_action(arg):
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
        has_mint_oga = bera.ooga_booga_contract.functions.hasMinted(account_address).call()
        ahoney_balance = bera.ahoney_contract.functions.balanceOf(account.address).call()
        domain_balance = bera.domain_contract.functions.balanceOf(account.address).call()
        if has_mint_oga and ahoney_balance > 0 and domain_balance > 0:
            append_data(private_key + ',,' + account_address)
            logger.success(
                f'第{index}次交互,{account_address},已经交互过了,耗时{time.time() - current_timestamp}')
        else:
            pass
    except Exception as e:
        logger.error(f'第{index}次交互,{account_address},{e}')


def get_app_item(values, index):
    if index in values:
        k = values[index]
    else:
        k = ''
    return k


def main(try_times, max_workers, mode_index, test_private_key_show):
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
    file_path_0 = 'wallet/bera_private_keys_hcy_auto_all_ok.txt'
    args_0 = []
    with open(file_path_0, 'r') as file:
        for private_key in file:
            private_key_str = private_key.strip()
            private_key_item = private_key_str.split(",")
            private_key_show = private_key_item[0]
            args_0.append(private_key_show)

    args = []
    with open(file_path, 'r') as file:
        op = 0
        for private_key in file:
            private_key_str = private_key.strip()
            private_key_item = private_key_str.split(",")
            private_key_show = private_key_item[0]
            if len(test_private_key_show) > 0:
                private_key_show = test_private_key_show
            if private_key_show not in args_0:
                args.append([private_key_show, get_rand_rpc(rpc_url, rpc_list), proxy_url, solver_provider, client_key,
                             try_times])
            op += 1
            if len(test_private_key_show) > 0:
                break
    random.shuffle(args)
    logger.debug(f'等待执行任务的地址数为{len(args)}')
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
        only_check_gas,  # 10 只检测gas
        check_all_action,  # 11 检查是否完成任务
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 将任务提交给线程池
        results = list(executor.map(mode_list[mode_index], args2))


if __name__ == '__main__':
    claim_mode = False  # 只批量领水
    test_private_key_show = ''  # 测试私钥
    for i in range(1):
        if claim_mode:
            main(5, 5, 0, test_private_key_show)  # 领水
            break
        # main(5, 5, 5, test_private_key_show)  # 只兑换
        # main(5, 5, 1, test_private_key_show)  # 只兑换
        # main(5, 5, 2, test_private_key_show)  # 只交换Hoeny和USDC
        # main(5, 5, 3, test_private_key_show)  # 只mintNFT,要有足够的Honey
        # main(5, 5, 8, test_private_key_show)  # 只发送铭文/只交互域名/只部署合约/只借贷
        #
        main(5, 12, 11, test_private_key_show)
        main(5, 12, 9, test_private_key_show)
        # main(5, 15, 6, test_private_key_show)
