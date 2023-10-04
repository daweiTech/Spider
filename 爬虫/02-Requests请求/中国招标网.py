# -*- coding: utf-8 -*-
# @Time    : 2022/7/27 9:24
# @Author  : 4v1d
# @File    : 中国招标网.py
# @Software: PyCharm

import requests
from lxml import html
etree = html.etree

def main():
    url = 'http://zb.yfb.qianlima.com/yfbsemsite/mesinfo/zbpglist'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
    count = 1
    while True:
        try:
            parse_rule1 = '//*[@id="contentTable"]/tbody/tr[{}]/td[1]/text()'.format(count)
            parse_rule2 = '//*[@id="contentTable"]/tbody/tr[{}]/td[2]/text()'.format(count)
            parse_rule3 = '//*[@id="contentTable"]/tbody/tr[{}]/td[3]/text()'.format(count)
            parse_rule4 = '//*[@id="contentTable"]/tbody/tr[{}]/td[4]/a/text()'.format(count)
            response = requests.get(url=url,headers=headers)
            ttime = etree.HTML(response.text).xpath(parse_rule1)[0]
            city_name = etree.HTML(response.text).xpath(parse_rule2)[0]
            ttype = etree.HTML(response.text).xpath(parse_rule3)[0]
            introduction = etree.HTML(response.text).xpath(parse_rule4)[0]
            intro = introduction.strip()
            print(ttime,city_name,ttype,intro)
            count+=1
        except:
            break

if __name__ == '__main__':
    main()