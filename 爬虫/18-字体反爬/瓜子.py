# -*- coding: utf-8 -*-
# @Time    : 2022/9/10 15:16
# @Author  : 4v1d
# @File    : 瓜子font.py
# @Software: PyCharm
import requests

def get_html():
    # 第1步：获取html，且存为html文件以便后面研究使用
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    }
    url = 'https://www.guazi.com/buy?search=%257B%2522minor%2522%253A%2522dazhong%2522%257D'
    ret = requests.get(url=url, headers=headers).text
    with open('guazi.html', 'w', encoding='utf8') as f:
        f.write(ret)
    return ret
get_html()