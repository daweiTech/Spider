# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 9:36
# @Author  : 4v1d
# @File    : Xpath1.py
# @Software: PyCharm
from lxml import html
etree = html.etree
from bases import Spiders
res = Spiders().fetch('https://pic.netbian.com/4kmeinv/index.html')
html = etree.HTML(res.text)
href = html.xpath('//div[@class="page"]/a[last()]/@href')
print(href)


from bs4 import BeautifulSoup

res = Spiders().fetch('https://movie.douban.com/chart')

soup1 = BeautifulSoup(res.text, 'lxml')
text = soup1.select('.nbg')
for i in text:
    print(i.text)