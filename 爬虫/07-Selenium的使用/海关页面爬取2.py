
from xl_utils import bases
from lxml import html
etree = html.etree

import requests


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

data = {
    "__RequestVerificationToken": "VBnwH_Jkg7gvjaRS3AUJO3OWdy1K-eABwrMou8NdM3kVdptDhi7NVBheK9c1_-SElpxziwxZSmH4s85g01NDT-Z9HYBGX3jLsPn3KcMb4fA1",
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
url = 'http://gss.customs.gov.cn/clsouter2020/Home/ClassifyYCDSearch'
r = bases.Spiders().fetch(url=url)
print(r.text)
import re
ver = re.findall('<input name="__RequestVerificationToken" type="hidden" value="(.*)" />',r.text)
print(ver[0])
data['__RequestVerificationToken'] = ver[0]
# response = requests.post(url=url, headers=headers, data=data, verify=False)
# print(data)

# url1 = 'http://gss.customs.gov.cn/CLSouter2020/Search/GetQuerySearchList'
# response = requests.post(url=url1, headers=headers, data=data, verify=False)
# print(response.text)
