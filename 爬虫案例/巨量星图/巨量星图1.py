import requests,httpx
import base64

def des_data():
    data = {"group": "rpc-xl",
            "action": "des",
            "data": 'hot_list_id0service_methodGetHotListDataservice_nameauthor.AdStarAuthorServicesign_strict1tag61e541324fe6649d1b8a2ee3e39539b8836fb99e1538974d3ac1fe98'
            }
    res = requests.get("http://127.0.0.1:5620/business-demo/invoke",params=data)
    print(res.text)
    return res.json().get('data')

def get_data():
    url = 'https://www.xingtu.cn/h/api/gateway/handler_get/'
    params = {
    "hot_list_id": "0",
    "tag": "61e541324fe6649d1b8a2ee3",
    "service_name": "author.AdStarAuthorService",
    "service_method": "GetHotListData",
    "sign_strict": "1",
    }
    sign = des_data()
    params['sign'] = sign
    print(params)
    headers =  headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cookie": "gfpart_1.0.1.3914_220078=0; csrftoken=hy1s57iKQC9KAX0d2357MjLVP4Mekq1g; tt_webid=7138221735770686988; ttcid=bc263e3ca1e14c70881051fd42f0534518; MONITOR_WEB_ID=e9fd2cbd-0e3e-42a9-bf04-744323bf4983; s_v_web_id=verify_l7ie7tyo_0uDOcZOH_PHTz_4s8q_8djO_AQGP7sr8fBDg; _tea_utm_cache_2018=undefined; passport_csrf_token=011b2441ee6316f7994444dabd483fcd; passport_csrf_token_default=011b2441ee6316f7994444dabd483fcd; gfpart_1.0.1.3985_220078=0; csrf_session_id=df528c097ba1be28a5ca1e2f16dfbef3; tt_scid=ncAThJFs-EWeutqUOZXEAg6S7oar6mL4bOVybORvmxrz0B2DLhAhVADD.I0q0Lxdbb34; passport_auth_status=9094e81b2476e928ece33bb40bf580da%2C78d625dff2aff9975321578319dda9ab; passport_auth_status_ss=9094e81b2476e928ece33bb40bf580da%2C78d625dff2aff9975321578319dda9ab; sid_guard=910c36a6f16201b3c65e239fd6c954f2%7C1662115668%7C5183999%7CTue%2C+01-Nov-2022+10%3A47%3A47+GMT; uid_tt=d4e6b48057dbd54b2394eb1b45722403; uid_tt_ss=d4e6b48057dbd54b2394eb1b45722403; sid_tt=910c36a6f16201b3c65e239fd6c954f2; sessionid=910c36a6f16201b3c65e239fd6c954f2; sessionid_ss=910c36a6f16201b3c65e239fd6c954f2; sid_ucp_v1=1.0.0-KDFmYjNlNDJjZTgwOGI3OGQ0M2U1NmMzZmQyYTQ0OGUxOTZiNDFjZTQKFgitkcCHkIz7BxDUvseYBhimDDgIQCoaAmxmIiA5MTBjMzZhNmYxNjIwMWIzYzY1ZTIzOWZkNmM5NTRmMg; ssid_ucp_v1=1.0.0-KDFmYjNlNDJjZTgwOGI3OGQ0M2U1NmMzZmQyYTQ0OGUxOTZiNDFjZTQKFgitkcCHkIz7BxDUvseYBhimDDgIQCoaAmxmIiA5MTBjMzZhNmYxNjIwMWIzYzY1ZTIzOWZkNmM5NTRmMg; star_sessionid=910c36a6f16201b3c65e239fd6c954f2; gftoken=OTEwYzM2YTZmMXwxNjYyMTE1NjcwOTJ8fDAGBgYGBgY; pay_sessionid=8VRVlAED8Ap5FKAGJ1i21fHy9k1NQlKxCw8g3wT14DQrZtxla3ubl0OqYHyvh4I7",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    res = requests.get(url,params=params,headers=headers,)
    print(res.url)
    print(res.text)

# des_data()
get_data()