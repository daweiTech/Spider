import requests


headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
cookies = {
    "_lx_utm": "utm_source^%^3Dbing^%^26utm_medium^%^3Dorganic",
    "_lxsdk_cuid": "1833a4550c0c8-018b8851c1a86f-977173c-144000-1833a4550c1c8",
    "_lxsdk": "1833a4550c0c8-018b8851c1a86f-977173c-144000-1833a4550c1c8",
    "_hc.v": "4144fc4d-d7ed-b9b2-005b-e128516031d0.1663129965",
    "fspop": "test",
    "cy": "2",
    "cye": "beijing",
    "s_ViewType": "10",
    "Hm_lvt_602b80cf8079ae6591966cc70a3940e7": "1663129965,1663504441",
    "WEBDFPID": "30y1u8659v31562v1w0yv52xzy4589768164901z1x29795893350074-1978864525967-1663504525378KAESEIQfd79fef3d01d5e9aadc18ccd4d0c95077393",
    "Hm_lpvt_602b80cf8079ae6591966cc70a3940e7": "1663506503",
    "_lxsdk_s": "18350975c9a-fe5-a-635^%^7C^%^7C131"
}
url = "http://www.dianping.com/hangzhou/ch10"
response = requests.get(url, headers=headers, cookies=cookies, verify=False)

# print(response.text)
def put_html(ttf_dict):
    with open("dzdp.html", "r", encoding="utf-8") as f:
        html = f.read()
        for k, v in ttf_dict.items():
            html = html.replace(k, v)
        return html
print(put_html())
