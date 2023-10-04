# -*- coding: utf-8 -*-
# @Time    : 2022/8/5 11:38
# @Author  : 4v1d
# @File    : 作业6.py
# @Software: PyCharm
from bases import *
import pymongo
import json
import threading

def parse(number):
    data = {
        'prodCatid' : number
    }
    r = Spiders().fetch('http://www.xinfadi.com.cn/getCat.html', param=data)
    res = json.loads(r.text)
    # print(type(res))
    list1 = res.get('list')
    # print(list1)
    client = pymongo.MongoClient('127.0.0.1', port=27017)
    db = client.test1
    collection = db['北京新发地']  # 都可以
    for i in list1:
        collection.insert(i)

def run():
    l = []
    id_list = [1186,1187,1188,1189,1190,1203,1204]
    for j in id_list:
        t = threading.Thread(target=parse,args=(j,))
        t.start()
        l.append(t)
    for k in l:
        k.join()

if __name__ == '__main__':
    run()