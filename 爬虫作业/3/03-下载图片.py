# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 22:59
# @Author  : 4v1d
# @File    : 03-下载图片.py
# @Software: PyCharm
import re
import os
import httpx
import requests
from pyquery import PyQuery as pq

#创建类Spider
class Spider():
    def __init__(self,list):#初始化url列表
        self.url_list = list

    def saveImg(self,index,byte):#字节形式保存图片，先判断当前目录下是否有image文件夹
        if os.path.exists("./image") is False:
            os.mkdir('./image')
        with open('./image/{}.jpg'.format(str(index)), 'wb') as f:
            f.write(byte)

    def crawler(self):#通过列表不断爬取
        urllist = self.url_list
        for index,u in enumerate(urllist):
            data = httpx.get(u)
            self.saveImg(index,data.content)

if __name__ == '__main__':
    r = requests.get('https://pic.netbian.com/')
    r.encoding = 'gbk'
    r1 = pq(r.text)
    r2 = r1('div.slist')
    result = re.findall('<img src="(.*?)>', str(r2))#正则提取出图片路径
    url_list = []
    for i in result:
        url = ('https://pic.netbian.com/' + i[1:48])
        url_list.append(url)
    Spider(url_list).crawler()

