# -*- coding: utf-8 -*-
# @Time    : 2022/8/4 19:29
# @Author  : 4v1d
# @File    : 爬取代理ip.py
# @Software: PyCharm

from bases import *
r = Spiders().fetch('https://www.zdaye.com/gansu_ip.html')
from lxml import html
etree = html.etree

html = etree.HTML(r.text)
url_list = html.xpath('//div[@class="top"]/div[@class="abox ov"]/div[@id="linklist"]/a/@href')
#url_list 列表
datalist = []
for i in url_list:
    url = 'https://www.zdaye.com' + i
    try:
        res = Spiders().fetch(url)
        html1 = etree.HTML(res.text)
        info = html1.xpath('//div[@class="top"]//tr/td/text()')
        print(info)
        datalist.append(info)
    except:
        pass

print(datalist)


import pymysql
db = pymysql.connect(host='127.0.0.1', user='root', password='root', port=3306, db='xyc')
cursor = db.cursor()  # 游标
