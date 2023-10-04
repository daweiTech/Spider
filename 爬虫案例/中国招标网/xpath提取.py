# -*- coding: utf-8 -*-
# @Time    : 2022/8/20 14:31
# @Author  : 4v1d
# @File    : 翻页测试.py
# @Software: PyCharm

import requests
from lxml import html
etree = html.etree

def main():
    for i in range(1,3):
        url = 'http://zb.yfb.qianlima.com/yfbsemsite/mesinfo/zbpglist'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
            }
        params = {
        "pageNo": "{}".format(i),
        "kwname": "",
        "pageSize": "15",
        "ipAddress": "120.40.220.145",
        "searchword": "",
        "searchword2": "",
        "hotword": "",
        "provinceId": "",
        "provinceName": "",
        "areaId": "",
        "areaName": "",
        "infoType": "1",
        "infoTypeName": "",
        "noticeTypes": "0",
        "noticeTypesName": "",
        "secondInfoType": "",
        "secondInfoTypeName": "",
        "timeType": "2",
        "timeTypeName": "",
        "searchType": "2",
        "clearAll": "false",
        "e_keywordid": "",
        "e_creative": "",
        "flag": "0",
        "source": "baidu",
        "firstTime": "1"
    }
        response = requests.get(url=url, headers=headers,params=params)
        source= etree.HTML(response.text)
        lis = source.xpath('//div[@class="select_box"]//tbody/tr')
        #print(lis)
        for j in lis:
            parse_rule1 = './td[1]/text()'
            parse_rule2 = './td[2]/text()'
            parse_rule3 = './td[3]/text()'
            parse_rule4 = './td[4]/a/text()'
            ttime = j.xpath(parse_rule1)[0]
            city_name =j.xpath(parse_rule2)[0]
            ttype = j.xpath(parse_rule3)[0]
            introduction = j.xpath(parse_rule4)[0]
            intro = introduction.strip()
            print(ttime,city_name,ttype,intro)


if __name__ == '__main__':
    main()