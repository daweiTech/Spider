# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 21:54
# @Author  : 4v1d
# @File    : 筛选ip.py
# @Software: PyCharm
import json
import time
import datetime
import redis
import requests
import threading

client = redis.Redis(host='192.168.40.128', port=6379, decode_responses=True,db=0)
zlist = client.zrangebyscore('proxies:universal',0,10)
print(zlist)
#print(zlist)

datalist = []
def verify_Ip(ip):
    proxy = {
            'http':'http://{}'.format(ip)
        }
    try:
        print(f'Threading {threading.current_thread().name} is running')
        r = requests.get(url='http://httpbin.org/get', proxies=proxy).text
        doc = json.loads(r)
        data = doc['origin']
        arr = data.split(',')
        if len(arr) == 2:
            client.zrem('proxies:universal',ip)
        else:
            datalist.append(arr[0])
            print("添加成功ip: {}".format(ip))
    except:
        client.zrem('proxies:universal',ip)

if __name__ == '__main__':
    start = datetime.datetime.now()
    print("开始时间{}".format(start))
    t = []
    for i in range(len(zlist)):
        thread = threading.Thread(target=verify_Ip, args=(zlist[i],))
        t.append(thread)
        thread.start()
    for i in t:
        i.join()
    end = datetime.datetime.now()
    print("结束时间{}".format(start))
    print(end - start, '多线程')
    print(datalist)