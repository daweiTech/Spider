import requests

headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "sec-ch-ua": "^\\^",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "elastic-apm-traceparent": "00-304ab6e4e412ceeb32ed31a7e67583d5-caa0bece5ca0864b-01",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://xueqiu.com/",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
cookies = {
    "device_id": "eab3ac2a7d2cbe64793aeccf0149b426",
    "acw_tc": "276077a116619949063542185e832a2cd7f4e9c06a333a3c36db6f84582c74",
    "xq_a_token": "45c480b02f280aa5399cbb8b545dbdfb8df3758b",
    "xqat": "45c480b02f280aa5399cbb8b545dbdfb8df3758b",
    "xq_r_token": "51853a11eb578337c65418905433e0ee029472fb",
    "xq_id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY2NDQwOTQ1MSwiY3RtIjoxNjYxOTk0OTAzNjczLCJjaWQiOiJkOWQwbjRBWnVwIn0.cLcddDExggYsWOkYtEaQyoBkO4lDXpH4VzpwR7Yn_GRkVGCivmSCV6emOPlq_n1r9inKXTAeofkUXXOUP7rucKTRMfasqO1P4bekynpJetfcbZdQcEdtZgJs3RUT7ENtBp-Jf2OZMCIMbH7q3OlYUmQmLluUy01cjh0qR42M2dZ4YRyyRtDKSvoP0ScAhi37UWyfWD4A8U7TW6JuXQjIatkXYqJ0HykmL37SbhNwzGcKpn7IIoOU0Be77weZTubu4rzmox0xrW6pIcQl93uhsUcXAl50OMlAIqmvvcNBGrHhAUstbDwVCWtLjidY0kEECRp8BKfENi8rD1uORn4sfw",
    "u": "381661994906364",
    "Hm_lvt_1db88642e346389874251b5a1eded6e3": "1661522155,1661994909",
    "Hm_lpvt_1db88642e346389874251b5a1eded6e3": "1661995140"
}
url = "https://xueqiu.com/statuses/hot/listV2.json"
params = {
    "since_id": "-1",
    "max_id": "390811",
    "size": "15"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)