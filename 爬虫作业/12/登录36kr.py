import time
import requests
import execjs
import json

r = open('36kr1.js',encoding='utf-8').read()
phone = execjs.compile(r).call('get_phone')
pwd = execjs.compile(r).call('get_pwd')
timestamp  = execjs.compile(r).call('get_timestamp')
data = {
    "krtoken": "",
    "param": {
        "countryCode": "86",
        "mobileNo": phone,
        "password": pwd
    },
    "partner_id": "web",
    "timestamp": timestamp
}
header = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-length": "460",
    "content-type": "application/json",
    "cookie": "sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22182d4d861371a4-0b3250a7fcbd2a-977173c-1327104-182d4d86139245%22%2C%22%24device_id%22%3A%22182d4d861371a4-0b3250a7fcbd2a-977173c-1327104-182d4d86139245%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_1684191ccae0314c6254306a8333d090=1661428327; Hm_lpvt_1684191ccae0314c6254306a8333d090=1661428327; Hm_lvt_713123c60a0e86982326bae1a51083e1=1661428327; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1661428327; acw_tc=2760777e16614283272437165e70fc8a1bd14de78e4c001c1aa6b6d3bcd682",
    "origin": "https://36kr.com",
    "pragma": "no-cache",
    "referer": "https://36kr.com/",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
def get_timestamp():
    return int(time.time() * 1000)
def login():
    url = 'https://gateway.36kr.com/api/mus/login/byMobilePassword'
    param = json.dumps(data)
    r = requests.post(url = url,headers = header,data=param)
    print(r.json())
login()