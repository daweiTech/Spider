# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 14:58
# @Author  : 4v1d
# @File    : 微榜2.py
# @Software: PyCharm
import csv,time
import requests,execjs


def getParams():
    with open(r"www.js", 'r', encoding='utf-8') as f:
        content = f.read()  # 读取js文件的全部内容到content变量中
    ctx = execjs.compile(content)
    jscode = 'get_nonce()'
    nonce = ctx.eval(jscode)
    pwd = 'b("/xdnphb/main/v1/weibo_day/rank?AppKey=joker&end=2022-09-04&rank_name=个人认证&rank_name_group=&start=2022' \
          '-09-04&nonce={}")'.format(nonce)
    xyz = ctx.eval(pwd)
    print(nonce)
    print(xyz)
    return nonce, xyz

def setData(**kwargs):
    data.update(kwargs)
    # print(data)

data={
    "end": "2022-09-04",
    "rank_name": "个人认证",
    "rank_name_group": "",
    "start": "2022-09-04",
    "nonce": "69525f8c7",
    "xyz": "b90b3974d36ac2e2e033691475f80631"
}
header={
            "origin":"https://www.newrank.cn",
            "referer":"https://www.newrank.cn/public/news.html?",
            "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent":"Mozilla/5.0"
        }


def getRank():
    session = requests.session()
    url = 'https://www.newrank.cn/xdnphb/main/v1/weibo_day/rank'
    nonce, xyz = getParams()
    setData(nonce=nonce, xyz=xyz)
    res = session.post(url=url, headers=header, data=data).json()
    return res


source = getRank()
rank_list = source.get('value')
for i in rank_list['datas']:
    name = i['name']
    followers = i['followers_count']
    likes = i['like_count']
    comment = i['comments_count']
    respost = i['reposts_count']

    item = {
        '作者':name,
        '粉丝':followers,
        '点赞':likes,
        '评论':comment,
        '转发':respost
    }
    print(item)
