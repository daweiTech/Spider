# -*- coding: utf-8 -*-
import requests


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "If-Modified-Since": "Wed, 01 Mar 2023 02:06:01 GMT",
    "If-None-Match": "W/^\\^63feb309-4c527^^",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "sec-ch-ua": "^\\^Not_A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^"
}
cookies = {
    "log": "",
    "cmsad_160_0": "0",
    "cmsad_156_0": "0",
    "cmsad_150_0": "0",
    "cmsad_152_0": "0",
    # "v": "A3OoH6umFOQAzNiwpnkIkY3bAnyYqAdlwTxLniUQzxLJJJ1irXiXutEM2-E2",
    "Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1": "1677632881,1677633628,1677636409",
    "Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1": "1677636409",
    "Hm_lvt_f79b64788a4e377c608617fba4c736e2": "1677632881,1677633631,1677636409",
    "Hm_lpvt_f79b64788a4e377c608617fba4c736e2": "1677636409"
}
url = "https://www.10jqka.com.cn/"
response = requests.get(url, headers=headers, cookies=cookies)
response.encoding = "gbk"
print(response.text)
print(response)