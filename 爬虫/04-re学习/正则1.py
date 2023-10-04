# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 8:10
# @Author  : 4v1d
# @File    : 正则1.py
# @Software: PyCharm

#\s 空白，\d 数字
import re
content = 'Hello 123 456 welcome to tuling'
result = re.match('^Hello\s\d\d\d',content)
print(result)
content1 = 'Hello 123456 welcome to tuling'
result1 = re.match('^Hello\s(\d+)\swelcome',content1)
print(result1.group(1))

data = 'resuly:{"1":"hh"}'
result2 = re.search('{.*?}',data)
print(result2.group())


import json
from bases import *
res = Spiders().fetch('https://finance.ifeng.com/c/8HzuiuhWgVRE')
s = re.findall('var allData = {(.*)};',res.text)
s1 = re.findall('var allData = {.*};',res.text)
#print(s)
import demjson
s2 = demjson.encode(s[0])
s3 = json.loads(s2)
print(s3)

#[\u4e00-\u9fa5]
s4 = '大家晚上好asdasdsad'
aa = re.findall('[\u4e00-\u9fa5]+',s4)
print(aa)

from pyquery import PyQuery as pq
url1 = 'https://www.baidu.com'
doc = pq(url=url1)
print(doc('title'))  # 根据标记提取


# CSS选择器， . class    # id