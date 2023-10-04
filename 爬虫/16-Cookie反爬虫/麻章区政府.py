import re
import httpx
from xl_utils import bases
ua = bases.FakeChromeUA()

def get_ck():
    url = 'http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc'
    res = httpx.request('GET',url)
    cookie = res.cookies.get('szxx_session')
    token = re.findall(r"var _CSRF = '(.*?)';",res.text)[0]
    return cookie,token

def index():
    c, t = get_ck()
    url = 'http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList'
    headers = {
        'user-agent': ua.get_ua(),
        'X-CSRF-TOKEN': t,
        'Cookie': 'XSRF-TOKEN={};szxx_session={}'.format(t, c)
    }
    data = {
        "offset": "0",
        "limit": "20",
        "site_id": "759010",
    }
    res = httpx.post(url,data=data,headers=headers)
    if res.status_code == 200:
        print(res.text)
    else:
        print('请求错误')

index()