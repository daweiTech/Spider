# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 16:20
# @Author  : 4v1d
# @File    : 单网页.py
# @Software: PyCharm

from bases import Spiders
from lxml import html
etree = html.etree

url = 'https://finance.ifeng.com/c/8HwI289ImHW'
res = Spiders().fetch(url)
html = etree.HTML(res.text)
content = html.xpath('//div[@class="text-3w2e3DBc"]/p/text()')
# for i in content[3:]:
print(content)
#     print(i)
# s = ''.join(content[3:])
# print(s)