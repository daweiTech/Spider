import re
import requests
import execjs

url = 'https://sh.esfxiaoqu.zhuge.com/page2/'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "sh.esfxiaoqu.zhuge.com",
    "Pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

r = requests.get(url=url,headers=headers)
complete_cookie = {}
complete_cookie.update(r.cookies.get_dict())
arg1 = re.findall("arg1='(.*)'",r.text)

with open('cccokie.js', 'r', encoding='utf-8') as f:
        acw_sc_v2_js = f.read()
acw_sc__v2 = execjs.compile(acw_sc_v2_js).call('xl', arg1[0])
complete_cookie.update({"acw_sc__v2": acw_sc__v2})
# 第二次访问首页，获取其他 cookies
response2 = requests.get(url=url, headers=headers, cookies=complete_cookie)
complete_cookie.update(response2.cookies.get_dict())
print(complete_cookie)

response3 = requests.get(url=url, headers=headers, cookies=complete_cookie)
response3.encoding = 'utf-8'
print(response3.text)
