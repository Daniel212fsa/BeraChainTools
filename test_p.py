# pip install requests
import requests

proxy_url = "http://XLl7km3ffMpqCrDTImLfPA:@smartproxy.crawlbase.com:8012"
proxies = {"http": proxy_url, "https": proxy_url}

response = requests.get(url="http://httpbin.org/ip", proxies=proxies, verify=False)

print('Response Code: ', response.status_code)
print('Response Body: ', response.content)