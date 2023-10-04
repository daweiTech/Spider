# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 22:46
# @Author  : 4v1d
# @File    : 筛选ip1.py
# @Software: PyCharm
from multiprocessing import Pool
import multiprocessing
import redis
import requests
import json

client = redis.Redis(host='192.168.40.128', port=6379, decode_responses=True,db=0)
zlist = client.zrangebyscore('proxies:universal',0,10)

def verify_Ip(ip):
    proxy = {
            'http':'http://{}'.format(ip)
        }
    try:
        r = requests.get(url='http://httpbin.org/get', proxies=proxy).text
        doc = json.loads(r)
        data = doc['origin']
        arr = data.split(',')
        if len(arr) == 2:
            client.zrem('proxies:universal',ip)
        else:
            print(r)
    except:
        client.zrem('proxies:universal',ip)

def run():
    import time
    s = time.time()
    cpu_count = multiprocessing.cpu_count()
    print("CPU 核心数量是：", cpu_count)
    pool = Pool(processes=8) # 8个进程
    for i in range(len(zlist)):
        pool.apply_async(verify_Ip, (zlist[i],))
    pool.close()  # 关闭进程池，关闭之后，不能再向进程池中添加进程
    pool.join()  # 当进程池中的所有进程执行完后，主进程才可以继续执行。
    print('程序耗时{}'.format(time.time() - s))

if __name__ == '__main__':
    run()
