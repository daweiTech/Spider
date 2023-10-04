
# -*- coding: utf-8 -*-
import requests

body = {
    "__RequestVerificationToken": "q0PHX8Q2DqkNc1LooTGpuJChhMz9gK6POi7bWHsYBYxHroVsu_hrr4itf-rX12w2gWMclRYjOvs_eU6B1bY2Blc5TXpg1s9gxnc3u1KUiw01",
    "page": "2",
    "pageSize": "20",
    "Type": "YCD",
    "SourceNo": "",
    "GName": "",
    "CodeTS": "",
    "GMdel": "",
    "EngName": "",
    "OtherName": ""
}

# 1.获取请求头中的cookie
def get_cookie():
    # 创建session对象，使用session发送post请求来获取cookie的值
    url = 'http://gss.customs.gov.cn/CLSouter2020/Search/GetQuerySearchList'
    session = requests.Session()
    session.post(url, data=body)
    request_cookies = session.cookies.get_dict()
    # print(request_cookies)  #可以打印出来看下有没有获取到
    return request_cookies

def get_cookies():
    # 创建session对象
    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://gss.customs.gov.cn",
        "Referer": "http://gss.customs.gov.cn/clsouter2020/Home/ClassifyYCDSearch",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    session = requests.Session()
    url = 'http://gss.customs.gov.cn/CLSouter2020/Search/GetQuerySearchList'
    # 使用session发送post请求获取cookie
    session.post(url, data=body,headers=headers)
    return session.cookies.get_dict()

# print(get_cookies())
# import tempfile
#
# a = tempfile.gettempdir()
# print(a)
from fake_useragent import UserAgent
import requests
def get_Cookies1():
    ua = UserAgent().ie
    headers = {'User-Agent': ua}
    url = 'http://gss.customs.gov.cn/CLSouter2020/Search/GetQuerySearchList'
    res = requests.get(url,headers=headers)
    cookiejar = res.cookies
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    print (cookiejar)
    print(cookiedict)

get_Cookies1()
