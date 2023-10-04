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
cookies = {
    "__RequestVerificationToken_L0NMU291dGVyMjAyMA2": "iCpCLQ-x5c8Zdaj3D4UEDDo-Hh70WNITIEQ-bDJT7ajyJ9wO8gPPG_stREGtXwD8_OiNHOXWO54gYwsV7ZdhV6rmM3JIf6LIjoycjN2U7Js1",
    "__jsluid_h": "ac5e34d4db77098e266c6754ebee7430"
}
url = "http://gss.customs.gov.cn/CLSouter2020/Search/GetQuerySearchList"
data = {
    "__RequestVerificationToken": "bFgFZm17cS2gr4NGcZqOwDwkFqfHf8VQtlHhcoEC0fyXyh80WnMZjflRiCv60Lp4thGC2n5D2v7y9ONNkRrzxUmHpvfhBTRfqcShUGxTNIs1",
    "page": "1",
    "pageSize": "20",
    "Type": "YCD",
    "SourceNo": "",
    "GName": "",
    "CodeTS": "",
    "GMdel": "",
    "EngName": "",
    "OtherName": ""
}
response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)

print(response.text)
print(response)