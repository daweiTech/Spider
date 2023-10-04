# -*- coding: utf-8 -*-
# @Time    : 2022/9/11 10:56
# @Author  : 4v1d
# @File    : 山东省统一.py
# @Software: PyCharm


import requests
from lxml import html
etree = html.etree

url = 'https://zwfw.sd.gov.cn/JIS/front/login.do'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "_pubk=048895ae09bcdb92f2cc0979954908acc9b9ab3fbc1b40904578c90e47d0c00e8a0d85b5d1a117ffb402e57d039f695f2776060992eac006179f606c277446fd0b; pageUrl=https%3A%2F%2Fzwfw.sd.gov.cn%2FJIS%2Ffront%2Flogin.do; TYSFRZ-CUSSESSIONID=5b22c8ec-e6d7-4f41-b6a1-c682e17d21d3",
    "Host": "zwfw.sd.gov.cn",
    "Pragma": "no-cache",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
r = requests.get(url=url,headers=headers)
source = etree.HTML(r.text)
img_url = source.xpath('//*[@id="verifyImg"]/@src')
# print(img_url)
base_url = 'https://zwfw.sd.gov.cn/JIS'
last_url = base_url + img_url[0][2:]
print(last_url)
r1 = requests.get(url=last_url,headers=headers)
import os
if os.path.exists("./image") is False:
    os.mkdir('./image')
with open('./image/{}.jpg'.format(str('code')), 'wb') as f:
    f.write(r1.content)
import ddddocr
ocr = ddddocr.DdddOcr()
with open("image/code.jpg", 'rb') as f:
    img_bytes = f.read()
red = ocr.classification(img_bytes)
print(red)