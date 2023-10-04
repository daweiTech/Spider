# -*- coding: utf-8 -*-
# @Time    : 2022/9/19 16:36
# @Author  : 4v1d
# @File    : dzdp-spider.py
# @Software: PyCharm
import requests


headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "sec-ch-ua": "^\\^",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
cookies = {
    "_lxsdk_cuid": "1833a4550c0c8-018b8851c1a86f-977173c-144000-1833a4550c1c8",
    "_lxsdk": "1833a4550c0c8-018b8851c1a86f-977173c-144000-1833a4550c1c8",
    "_hc.v": "4144fc4d-d7ed-b9b2-005b-e128516031d0.1663129965",
    "fspop": "test",
    "s_ViewType": "10",
    "WEBDFPID": "30y1u8659v31562v1w0yv52xzy4589768164901z1x29795893350074-1978864525967-1663504525378KAESEIQfd79fef3d01d5e9aadc18ccd4d0c95077393",
    "_lx_utm": "utm_source^%^3Dbing^%^26utm_medium^%^3Dorganic",
    "cy": "1",
    "cye": "shanghai",
    "Hm_lvt_602b80cf8079ae6591966cc70a3940e7": "1663571050,1663587602,1663663919,1663669165",
    "Hm_lpvt_602b80cf8079ae6591966cc70a3940e7": "1663680870",
    "_lxsdk_s": "1835b1892c1-a87-a97-29c^%^7C^%^7C35"
}
url = "https://www.dianping.com/shop/k3ZbV7SZiJdS33o8"
response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)
with open('222.html','w',encoding='utf-8') as f:
    f.write(response.text)
    f.close()
