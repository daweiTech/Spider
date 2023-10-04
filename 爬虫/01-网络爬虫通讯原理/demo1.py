# -*- coding: utf-8 -*-
# @Time    : 2022/7/24 15:46
# @Author  : 4v1d
# @File    : 中国招标网.py
# @Software: PyCharm

import httpx

url = 'https://www.baidu.com'

res = httpx.get(url)
print(res.text)