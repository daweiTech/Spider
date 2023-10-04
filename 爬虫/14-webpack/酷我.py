# -*- coding: utf-8 -*-
# @Time    : 2022/8/23 16:39
# @Author  : 4v1d
# @File    : 酷我.py
# @Software: PyCharm
import execjs
import requests
r = open('kuwo.js',encoding='utf-8').read()
source = execjs.compile(r).call('xl')
print(source)


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1661241476; _ga=GA1.2.934145329.1661241476; _gid=GA1.2.944234893.1661241476; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1661243785; kw_token=L9KN4A2BRL",
    "csrf": "L9KN4A2BRL",
    "Host": "www.kuwo.cn",
    "origin": "https://www.kuwo.cn/",
    "Pragma": "no-cache",
    "Referer": "https://www.kuwo.cn/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
params = {
    "bangId": "93",
    "pn": "1",
    "rn": "30",
    "httpsStatus": "1",
    "reqId": 'fa26f0a0-22be-11ed-8521-3bc7004cba45'
}
response = requests.get('http://www.kuwo.cn/api/www/bang/bang/musicList'
                        '?bangId=93&pn=1&rn=30&httpsStatus=1&reqId=fa26f0a0'
                        '-22be-11ed-8521-3bc7004cba45',headers=headers,
                        params=params)
print(response.text)


