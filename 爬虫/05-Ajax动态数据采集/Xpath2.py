# -*- coding: utf-8 -*-
# @Time    : 2022/8/6 9:36
# @Author  : 4v1d
# @File    : Xpath2.py
# @Software: PyCharm
import requests

from lxml import html
etree = html.etree
from bases import *
#博客链接地址
r = Spiders().fetch('https://blog.csdn.net/weixin_51213906?type=blog')
html1 = etree.HTML(r.text)
url_list = html1.xpath('//article/a/@href')
print(url_list)
for i in url_list:
    Spiders().fetch(i)
"""
['https://blog.csdn.net/weixin_51213906/article/details/125905589', 'https://blog.csdn.net/weixin_51213906/article/details/125889484', 'https://blog.csdn.net/weixin_51213906/article/details/124654275', 'https://blog.csdn.net/weixin_51213906/article/details/124616210', 'https://blog.csdn.net/weixin_51213906/article/details/124590061', 'https://blog.csdn.net/weixin_51213906/article/details/124541520', 'https://blog.csdn.net/weixin_51213906/article/details/124541232', 'https://blog.csdn.net/weixin_51213906/article/details/124483076', 'https://blog.csdn.net/weixin_51213906/article/details/124482508', 'https://blog.csdn.net/weixin_51213906/article/details/124481641', 'https://blog.csdn.net/weixin_51213906/article/details/123585647', 'https://blog.csdn.net/weixin_51213906/article/details/123310062']

"""