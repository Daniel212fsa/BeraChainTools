# -*- coding: cp936 -*-
import requests
from loguru import logger


#���ж���
def get_proxy():
    proxy_url = ''
    aaa = requests.get(proxy_url).text
    proxy_host = aaa.splitlines()[0]
    logger.debug('����IPΪ��' + proxy_host)
    proxy = {
        'http': 'http://' + proxy_host,
        'https': 'http://' + proxy_host
    }
    return proxy
