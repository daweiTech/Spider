import requests

proxypool_url = 'http://192.168.40.128:5555/random'
target_url = 'http://httpbin.org/get'

def get_random_proxy():
    """
    get random proxy from proxypool
    :return: proxy
    """
    return requests.get(proxypool_url).text.strip()

def crawl(url, proxy):
    """
    use proxy to crawl page
    :param url: page url
    :param proxy: proxy, such as 8.8.8.8:8888
    :return: html
    """
    proxies = {'http': 'http://' + proxy}
    return requests.get(url, proxies=proxies).text


def main():
    """
    main method, entry point
    :return: none
    """
    proxy = get_random_proxy()
    print('get random proxy', proxy)
    html = crawl(target_url, proxy)
    print(html)

if __name__ == '__main__':
    proxy = {
        'http':'http://58.246.58.150:9002'
    }
    r = requests.get(url='http://httpbin.org/get',proxies=proxy).text
    print(r)
    # import redis
    # client = redis.Redis(host='192.168.40.130', port=6379, decode_responses=True, db=0)
    # client.zrem('proxies:universal',10)
    # # list = [1,2,3,4,5]
    # # print(list[2:])
    # import json
    # doc = json.loads(r)
    # print(type(doc))
#     datalist = []
#     dict = {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Cache-Control": "max-age=259200",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.27.0",
#     "X-Amzn-Trace-Id": "Root=1-62f8f7ac-4296bf8642f46cab58659334"
#   },
#   "origin": "47.243.99.43",
#   "url": "http://httpbin.org/get"
# }
#     data = dict['origin']
#     arr = data.split(',')
#     if len(arr)==2:
#         pass
#     else:
#         datalist.append(arr[0])
#
#     print(datalist)


list = [{'http': 'http://58.220.95.34\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.34\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://39.130.150.42\xa0\xa0:80\xa0\xa0', 'https': 'https://39.130.150.42\xa0\xa0:80\xa0\xa0'}, {'http': 'http://183.250.163.175\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.250.163.175\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://211.142.96.250\xa0\xa0:9091\xa0\xa0', 'https': 'https://211.142.96.250\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://182.61.201.201\xa0\xa0:80\xa0\xa0', 'https': 'https://182.61.201.201\xa0\xa0:80\xa0\xa0'}, {'http': 'http://219.146.125.162\xa0\xa0:9091\xa0\xa0', 'https': 'https://219.146.125.162\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://183.239.55.65\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.239.55.65\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://111.21.183.58\xa0\xa0:9091\xa0\xa0', 'https': 'https://111.21.183.58\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://58.220.95.30\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.30\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://58.220.95.31\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.31\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://117.160.132.37\xa0\xa0:9091\xa0\xa0', 'https': 'https://117.160.132.37\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://112.5.56.2\xa0\xa0:9091\xa0\xa0', 'https': 'https://112.5.56.2\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://120.237.144.77\xa0\xa0:9091\xa0\xa0', 'https': 'https://120.237.144.77\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://223.94.85.131\xa0\xa0:9091\xa0\xa0', 'https': 'https://223.94.85.131\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://183.215.172.2\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.215.172.2\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://218.75.38.154\xa0\xa0:9091\xa0\xa0', 'https': 'https://218.75.38.154\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://218.201.77.143\xa0\xa0:9091\xa0\xa0', 'https': 'https://218.201.77.143\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://59.48.200.158\xa0\xa0:9091\xa0\xa0', 'https': 'https://59.48.200.158\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://61.145.111.9\xa0\xa0:443\xa0\xa0', 'https': 'https://61.145.111.9\xa0\xa0:443\xa0\xa0'}, {'http': 'http://58.220.95.8\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.8\xa0\xa0:10174\xa0\xa0'}]
[{'http': 'http://58.220.95.34\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.34\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://39.130.150.42\xa0\xa0:80\xa0\xa0', 'https': 'https://39.130.150.42\xa0\xa0:80\xa0\xa0'}, {'http': 'http://183.250.163.175\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.250.163.175\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://211.142.96.250\xa0\xa0:9091\xa0\xa0', 'https': 'https://211.142.96.250\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://182.61.201.201\xa0\xa0:80\xa0\xa0', 'https': 'https://182.61.201.201\xa0\xa0:80\xa0\xa0'}, {'http': 'http://219.146.125.162\xa0\xa0:9091\xa0\xa0', 'https': 'https://219.146.125.162\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://183.239.55.65\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.239.55.65\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://111.21.183.58\xa0\xa0:9091\xa0\xa0', 'https': 'https://111.21.183.58\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://58.220.95.30\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.30\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://58.220.95.31\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.31\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://117.160.132.37\xa0\xa0:9091\xa0\xa0', 'https': 'https://117.160.132.37\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://112.5.56.2\xa0\xa0:9091\xa0\xa0', 'https': 'https://112.5.56.2\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://120.237.144.77\xa0\xa0:9091\xa0\xa0', 'https': 'https://120.237.144.77\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://223.94.85.131\xa0\xa0:9091\xa0\xa0', 'https': 'https://223.94.85.131\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://183.215.172.2\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.215.172.2\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://218.75.38.154\xa0\xa0:9091\xa0\xa0', 'https': 'https://218.75.38.154\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://218.201.77.143\xa0\xa0:9091\xa0\xa0', 'https': 'https://218.201.77.143\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://59.48.200.158\xa0\xa0:9091\xa0\xa0', 'https': 'https://59.48.200.158\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://61.145.111.9\xa0\xa0:443\xa0\xa0', 'https': 'https://61.145.111.9\xa0\xa0:443\xa0\xa0'}, {'http': 'http://58.220.95.8\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.8\xa0\xa0:10174\xa0\xa0'}]
[{'http': 'http://58.220.95.34\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.34\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://39.130.150.42\xa0\xa0:80\xa0\xa0', 'https': 'https://39.130.150.42\xa0\xa0:80\xa0\xa0'}, {'http': 'http://183.250.163.175\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.250.163.175\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://211.142.96.250\xa0\xa0:9091\xa0\xa0', 'https': 'https://211.142.96.250\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://182.61.201.201\xa0\xa0:80\xa0\xa0', 'https': 'https://182.61.201.201\xa0\xa0:80\xa0\xa0'}, {'http': 'http://219.146.125.162\xa0\xa0:9091\xa0\xa0', 'https': 'https://219.146.125.162\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://183.239.55.65\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.239.55.65\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://111.21.183.58\xa0\xa0:9091\xa0\xa0', 'https': 'https://111.21.183.58\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://58.220.95.30\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.30\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://58.220.95.31\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.31\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://117.160.132.37\xa0\xa0:9091\xa0\xa0', 'https': 'https://117.160.132.37\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://112.5.56.2\xa0\xa0:9091\xa0\xa0', 'https': 'https://112.5.56.2\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://120.237.144.77\xa0\xa0:9091\xa0\xa0', 'https': 'https://120.237.144.77\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://223.94.85.131\xa0\xa0:9091\xa0\xa0', 'https': 'https://223.94.85.131\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://183.215.172.2\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.215.172.2\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://218.75.38.154\xa0\xa0:9091\xa0\xa0', 'https': 'https://218.75.38.154\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://218.201.77.143\xa0\xa0:9091\xa0\xa0', 'https': 'https://218.201.77.143\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://59.48.200.158\xa0\xa0:9091\xa0\xa0', 'https': 'https://59.48.200.158\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://61.145.111.9\xa0\xa0:443\xa0\xa0', 'https': 'https://61.145.111.9\xa0\xa0:443\xa0\xa0'}, {'http': 'http://58.220.95.8\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.8\xa0\xa0:10174\xa0\xa0'}]
[{'http': 'http://58.220.95.34\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.34\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://39.130.150.42\xa0\xa0:80\xa0\xa0', 'https': 'https://39.130.150.42\xa0\xa0:80\xa0\xa0'}, {'http': 'http://183.250.163.175\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.250.163.175\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://211.142.96.250\xa0\xa0:9091\xa0\xa0', 'https': 'https://211.142.96.250\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://182.61.201.201\xa0\xa0:80\xa0\xa0', 'https': 'https://182.61.201.201\xa0\xa0:80\xa0\xa0'}, {'http': 'http://219.146.125.162\xa0\xa0:9091\xa0\xa0', 'https': 'https://219.146.125.162\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://183.239.55.65\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.239.55.65\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://111.21.183.58\xa0\xa0:9091\xa0\xa0', 'https': 'https://111.21.183.58\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://58.220.95.30\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.30\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://58.220.95.31\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.31\xa0\xa0:10174\xa0\xa0'}, {'http': 'http://117.160.132.37\xa0\xa0:9091\xa0\xa0', 'https': 'https://117.160.132.37\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://112.5.56.2\xa0\xa0:9091\xa0\xa0', 'https': 'https://112.5.56.2\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://120.237.144.77\xa0\xa0:9091\xa0\xa0', 'https': 'https://120.237.144.77\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://223.94.85.131\xa0\xa0:9091\xa0\xa0', 'https': 'https://223.94.85.131\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://183.215.172.2\xa0\xa0:9091\xa0\xa0', 'https': 'https://183.215.172.2\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://218.75.38.154\xa0\xa0:9091\xa0\xa0', 'https': 'https://218.75.38.154\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://218.201.77.143\xa0\xa0:9091\xa0\xa0', 'https': 'https://218.201.77.143\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://59.48.200.158\xa0\xa0:9091\xa0\xa0', 'https': 'https://59.48.200.158\xa0\xa0:9091\xa0\xa0'}, {'http': 'http://61.145.111.9\xa0\xa0:443\xa0\xa0', 'https': 'https://61.145.111.9\xa0\xa0:443\xa0\xa0'}, {'http': 'http://58.220.95.8\xa0\xa0:10174\xa0\xa0', 'https': 'https://58.220.95.8\xa0\xa0:10174\xa0\xa0'}]