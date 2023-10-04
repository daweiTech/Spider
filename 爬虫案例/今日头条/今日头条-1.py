# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 22:26
# @Author  : 4v1d
# @File    : 今日头条-1.py
# @Software: PyCharm
# encoding: utf-8
"""
@author: 夏洛
@QQ: 1972386194
@file: 头条测试.py
"""

import urllib3,requests
urllib3.disable_warnings()

def get_sig(url):
    data = {
        "group": "tt-test",
        "action": "toutiao",
        "url": url
    }
    res = requests.post(url="http://127.0.0.1:5620/business-demo/invoke", data=data, verify=False)
    resp = res.json()
    if "?" in url:
        url += "&_signature={}".format(resp['signature'])
    else:
        url += "?_signature={}".format(resp['signature'])
    return url

url = get_sig('https://www.toutiao.com/api/pc/list/feed?offset=0&channel_id=94349549395&max_behot_time=0&category=pc_profile_channel&disable_raw_data=true&aid=24&app_name=toutiao_web')
print(url)

session = requests.session()
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
res = session.get(url,headers=headers)
if res.status_code == 200:
    if res.json().get('message') == 'success':
        items = res.json().get('data')
        for i in items:
            title = i.get('title')
            print(title)
