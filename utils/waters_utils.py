import time

from eth_account import Account
from loguru import logger
import requests
from bera_tools import BeraChainTools
import concurrent.futures
import redis


def get_proxy(proxy_url):
    aaa = requests.get(proxy_url).text
    proxy_host = aaa.splitlines()[0]
    logger.debug('代理IP为：' + proxy_host)
    proxy = {
        'http': 'http://' + proxy_host,
        'https': 'http://' + proxy_host
    }
    return proxy


def generate_wallet(count, rpc_url, proxy_url, solver_provider, client_key, file_path, max_workers):
    use_redis_mode = True
    if use_redis_mode:
        pool = redis.ConnectionPool(host='127.0.0.1')
        r = redis.Redis(connection_pool=pool)

    def generate_account(i):
        try:
            logger.debug(f'Generating account {i + 1}')
            account = Account.create()
            logger.debug(f'Address: {account.address}')
            logger.debug(f'Key: {account.key.hex()}')
            bera = BeraChainTools(private_key=account.key, proxy_url=proxy_url, client_key=client_key,
                                  solver_provider=solver_provider,
                                  rpc_url=rpc_url)

            proxies_to = {}
            if use_redis_mode:
                for i in range(10):
                    proxies = get_proxy(proxy_url)
                    is_used = r.get(proxies['http'])
                    if is_used is None:
                        r.set(proxies['http'], proxies['http'])
                        proxies_to = proxies
                        break
                    else:
                        logger.error(f'领水失败,代理重复了\n')
                        time.sleep(1)
            else:
                proxies = get_proxy(proxy_url)
                proxies_to = proxies

            if 'http' in proxies_to:
                result = bera.claim_bera(proxies=proxies_to)
                if 'Txhash' in result.text or 'to the queue' in result.text:
                    logger.success(f'领水成功,{result.text}\n')
                    with open(file_path, 'a') as f:
                        f.write(account.key.hex() + '\n')
                else:
                    logger.error(f'领水失败,{result.text}\n')
            else:
                logger.error(f'没有正确的代理')
        except Exception as e:
            logger.error(f'领水失败,{e}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(generate_account, range(count))
