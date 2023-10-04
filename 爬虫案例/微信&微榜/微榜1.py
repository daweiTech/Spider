# -*- coding: utf-8 -*-
# @Time    : 2022/9/4 23:30
# @Author  : 4v1d
# @File    : 微榜.py
# @Software: PyCharm

import csv,time
import requests,execjs
class xinbang:
    def __init__(self):
        self.session=requests.session()
        self.header={
            "origin":"https://www.newrank.cn",
            "referer":"https://www.newrank.cn/public/news.html?",
            "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent":"Mozilla/5.0"
        }
        self.data0={
            'nonce': '4881f2eed',
            'xyz': '875a6b0e32398455f083224be103a6fb'
        }
        self.data={
    "end": "2022-09-04",
    "rank_name": "个人认证",
    "rank_name_group": "",
    "start": "2022-09-04",
    "nonce": "69525f8c7",
    "xyz": "b90b3974d36ac2e2e033691475f80631"
}

    def setData0(self,**kwargs):
        self.data0.update(kwargs)
        print(self.data0)

    def setData(self,**kwargs):
        self.data.update(kwargs)
        print(self.data)

    def getParams(self):
        with open(r"www.js", 'r',encoding='utf-8') as f:
            content = f.read() #读取js文件的全部内容到content变量中
        ctx = execjs.compile(content)
        jscode = 'get_nonce()'
        nonce=ctx.eval(jscode)
        pwd='b("/xdnphb/main/v1/weibo_day/rank?AppKey=joker&end=2022-09-04&rank_name=个人认证&rank_name_group=&start=2022' \
            '-09-04&nonce={}")'.format(nonce)
        xyz=ctx.eval(pwd)
        print(nonce)
        print(xyz)
        return nonce,xyz

    def request(self):
        getUrl="https://www.newrank.cn/xdnphb/common/account/get"
        getFullUrl="https://www.newrank.cn/xdnphb/common/account/getFull"
        nonce,xyz=self.getParams()
        self.setData0(nonce=nonce,xyz=xyz)
        self.session.post(url=getUrl,headers=self.header,data=self.data)
        nonce, xyz =self.getParams()
        self.setData0(nonce=nonce,xyz=xyz)
        self.session.post(url=getFullUrl,headers=self.header,data=self.data)


    def getHtml(self,page):
        url = "https://www.newrank.cn/xdnphb/index/getMedia"
        nonce, xyz =self.getParams(page)
        self.setData(pageNumber=str(page),nonce=nonce,xyz=xyz)
        res=self.session.post(url=url, headers=self.header, data=self.data).json()
        print(res)
        return res

    def getRank(self):
        url = 'https://www.newrank.cn/xdnphb/main/v1/weibo_day/rank'
        nonce, xyz = self.getParams()
        self.setData(nonce=nonce, xyz=xyz)
        res = self.session.post(url=url, headers=self.header, data=self.data).json()
        print(res)
        return res
    def tocsv(self,res,csvwriter):
        value=res["value"]
        for each in value:
            title=each["title"]
            timer = each["public_time"]
            label=each["label"]
            author=each["author"]
            url=each["url"]
            csvwriter.writerow([title,label,timer,author,url])
            print([title,label,timer,author,url])

def main():
    start=time.time()
    xb=xinbang()
    xb.request()
    xb.getRank()

    print(time.time()-start)
if __name__=="__main__":
    main()
