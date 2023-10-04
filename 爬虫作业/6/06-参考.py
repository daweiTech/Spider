# -*- coding: utf-8 -*-
# @Time    : 2022/8/5 11:38
# @Author  : 4v1d
# @File    : 作业6.py
# @Software: PyCharm
import requests
import pymongo
import json
import time
from concurrent.futures.thread import ThreadPoolExecutor

#数据库连接
client = pymongo.MongoClient('127.0.0.1', port=27017)
db = client.Spiders
collection = db['北京新发地-8.5']  # 名字任意


def one_page(data:dict):
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "82",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.xinfadi.com.cn",
        "Origin": "http://www.xinfadi.com.cn",
        "Referer": "http://www.xinfadi.com.cn/priceDetail.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    }
    r = requests.post('http://www.xinfadi.com.cn/getPriceData.html', headers=header, data=data)
    res = json.loads(r.text)#json处理页面格式为字典
    list = res.get('list')
    for j in list:
        dict = {}
        dict['产品名字'] = j.get('prodName')
        dict['产品种类'] = j.get('prodCat')
        dict['最低价格'] = j.get('lowPrice')
        dict['最高价格'] = j.get('highPrice')
        dict['平均价格'] = j.get('avgPrice')
        dict['产地'] = j.get('place')
        dict['单位信息'] = j.get('unitInfo')
        dict['日期'] = j.get('pubDate')
        saveData(dict)

def list_page(page_start,page_end,page_limit:int=20):
    with ThreadPoolExecutor(100) as t:#构造线程池
        for i in range(page_start,page_end+1):
            data = {
    "limit": page_limit,
    "current": i,
    "pubDateStartTime": "",
    "pubDateEndTime": "",
    "prodPcatid": "",
    "prodCatid": "",
    "prodName": ""
}
            t.submit(one_page, data)#提交线程到线程池中

def run():#计算使用线程时长，大约十几秒
    start_time = time.time()
    list_page(page_start=1, page_end=100, page_limit=20)#定义翻页页数和每页爬取量，最大20
    end_time = time.time()
    print(f'总耗时{end_time - start_time}s')

def saveData(data):#存入Mongodb
    if isinstance(data, dict):
        collection.insert(data)

if __name__ == '__main__':
    run()

