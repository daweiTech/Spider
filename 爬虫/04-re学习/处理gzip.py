content = """
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
# print(content.encode('utf-8').decode('utf-8'))
data = """
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   _/ ____\____ _/ ____\_ __ 
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   __\\__  \\   __\  |  \
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |  |   / __ \|  | |  |  /
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   |__|  (____  /__| |____/ 
       \/       \/          \/            \/     \/                             \/              """
# print(data)

import requests
from urllib import request
import urllib
from io import BytesIO
import gzip
def send_wechat(msg):
    token = 'bbb40cfb0a8a4428b9cb9e62d0742c0d'#前边复制到那个token
    title = 'title1'
    content = msg
    template = 'html'
    url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
    print(url)
    r = requests.get(url=url)
    print(r.text)


def get_data():
  url = 'https://www.bibiqing.com/exchange/notice/list_1.html'
  headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "cookie": "Hm_lvt_391b48aeb4720d6605b50f1ea4540e36=1662995774; JSESSIONID=5b612ea5-09f0-4514-a1b0-49a1bf02d9a4; DTL_SESSION_ID=5b612ea5-09f0-4514-a1b0-49a1bf02d9a4; Hm_lpvt_391b48aeb4720d6605b50f1ea4540e36=1662996593",
    "pragma": "no-cache",
    "referer": "https://www.bibiqing.com/exchange/notice/",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
  r = request.urlopen(url)
  htmls = r.read()
  buff = BytesIO(htmls)
  f = gzip.GzipFile(fileobj=buff)
  htmls = f.read().decode('utf-8')
  print(r.text)


def open_page(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36")
    page = urllib.request.urlopen(req)

    if ('Content-Encoding', 'gzip') in page.headers._headers:
        # content是gzip压缩过的数据,所以需要对我们接收的字节码进行一个解码操作
        content = page.read()
        content = gzip.decompress(content).decode('utf-8')
    else:
        content = page.read().decode('utf-8')
    return content
if __name__ == '__main__':
    msg = 'Life is short I use python'
    # send_wechat(msg)

    # get_data()
    print(open_page('https://www.bibiqing.com/exchange/notice/list_1.html'))
    
