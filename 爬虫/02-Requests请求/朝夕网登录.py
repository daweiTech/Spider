# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 10:34
# @Author  : 4v1d
# @File    : 朝夕网登录.py
# @Software: PyCharm
import requests
import hashlib
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "cookie": "yizuotu_id=86DD4EFA-0799-4BFC-B809-F7BC54A1FAB3; __51vcke__JGpqj8ul83L3sRlp=4047d7ad-97a4-5b16-bdae-847fb28ddb50; __51vuft__JGpqj8ul83L3sRlp=1660571103201; __gads=ID=4261eff835a44d20-220987a49dd50004:T=1660571106:RT=1660571106:S=ALNI_MZzDXbuH9-DW_BodEe6-l_3mTVP1g; __gpi=UID=000008a2c0bcfa57:T=1660571106:RT=1660611692:S=ALNI_MYU0E-6wzTnYJGfCS0yJ3s3j-OgZQ; __51uvsct__JGpqj8ul83L3sRlp=3; Hm_lvt_62c11b29bc9bed764fa8f99bfa36fca2=1660571103,1660611693,1660617006; __vtins__JGpqj8ul83L3sRlp=%7B%22sid%22%3A%20%22340909bf-959f-56e3-a5e3-404a95963b27%22%2C%20%22vd%22%3A%202%2C%20%22stt%22%3A%20497830%2C%20%22dr%22%3A%20497830%2C%20%22expires%22%3A%201660619303550%2C%20%22ct%22%3A%201660617503550%7D; Hm_lpvt_62c11b29bc9bed764fa8f99bfa36fca2=1660617504",
    "pragma": "no-cache",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
# cookies =  {
#     'Hm_lvt_62c11b29bc9bed764fa8f99bfa36fca2': '1660572978',
#     'PHPSESSID': 'c6a8fui5qg5eu8u3pt2jbhjhj6',
#     'yizuotu_id': 'A5E875CF-3032-40EF-930E-F6E3412370D3',
#     '__gads': 'ID=cd8d1d47e0156492-22e8cfed99d500f3:T=1660572977:RT=1660572977:S=ALNI_MZLTR-EkgQHtctuDq-dtiHoMnm5mQ',
#     '__gpi': 'UID=000008a2cf6105c9:T=1660572977:RT=1660572977:S=ALNI_MYvZoIl6fw7zZBB339CnF2x2yZ-3A',
#     'Hm_lpvt_62c11b29bc9bed764fa8f99bfa36fca2': '1660573004',
# }
username = input('请输入用户名：')
password = input('请输入密码：')
pwd = hashlib.md5()
pwd.update(password.encode(encoding='utf-8'))
print(pwd.hexdigest())
data = {
    "action": "login",
    "txtusername": username,
    "txtpassword": pwd.digest()
}
url ='https://my.zhaoxi.net//diy/getlogin.php'
login = requests.post(url,headers = headers,data = data)
print(login.text)
# # 登录后，我们需要获取另一个网页中的内容
# response = session.get('https://my.zhaoxi.net//diy/getlogin.php',headers = headers)
# print(response.status_code)
# print(response.text)