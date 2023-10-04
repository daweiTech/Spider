# -*- coding: utf-8 -*-
# @Time    : 2022/7/29 9:40
# @Author  : 4v1d
# @File    : 04-saveDatatodatabase.py
# @Software: PyCharm

from bases import *
import pymysql
from dbutils.pooled_db import PooledDB
import requests
from lxml import html
etree = html.etree

res = Spiders().fetch('https://cs.fang.ke.com/loupan/')
html = etree.HTML(res.text)

h1 = html.xpath('//div[@class="resblock-name"]/a/text()')
print(h1)#名字
h2 = html.xpath('//div[@class="resblock-desc-wrapper"]/a/text()')
h2 = [x.strip() for x in h2 if x.strip()!='']
print(h2)#地址
# with open('test.html','r',encoding='utf-8') as f1 :
#     html1 = f1.read()
# html2 = etree.HTML(html1)
h3 = html.xpath('//div[@class="resblock-tag"]/span/text()')
print(h3)#标签
h4 = html.xpath('//span[@class="area"]/text()')
# h4 = [x for x in h4 if x!='暂无']
print(h4)#面积
h5 = html.xpath('//span[@class="resblock-type"]/text()')
print(h5)#状态

