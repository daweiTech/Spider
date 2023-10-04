# -*- coding: utf-8 -*-
# @Time    : 2022/9/4 15:58
# @Author  : 4v1d
# @File    : 同花顺.py
# @Software: PyCharm
# import execjs
#
# with open('同花顺.js',encoding='utf-8') as f:
#     x = f.read()
# # print(x)
# v = execjs.compile(x).call('get_Cookie')
# print(v)

import requests


headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Referer": "http://q.10jqka.com.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "hexin-v": "AyD7poRnV53_LeuZ5mkr-EoK8SX3KQQQpgxY5Zox7e3Phs4bQjnUg_YdKIHp"
}
cookies = {
    "log": "",
    "Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1": "1677632881,1677633628",
    "Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1": "1677633628",
    "v": "AyD7poRnV53_LeuZ5mkr-EoK8SX3KQQQpgxY5Zox7e3Phs4bQjnUg_YdKIHp"
}
url = "https://www.10jqka.com.cn/"
      #http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/2/ajax/1/
response = requests.get(url, headers=headers, cookies=cookies, verify=False)

print(response.text)





