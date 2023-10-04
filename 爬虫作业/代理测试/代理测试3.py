# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 7:52
# @Author  : 4v1d
# @File    : 测试模板.py
# @Software: PyCharm

import requests
from lxml import html
etree = html.etree

base_url = 'https://www.zdaye.com'
url = 'https://www.zdaye.com/dayProxy.html'
pro = {
    'http':'http://116.202.13.106:9999'
}
header = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'}

proxies_list = []

res = requests.get(url, headers=header)
print(res.status_code)
res.encoding = 'utf-8'
dom = etree.HTML(res.text)
sub_urls = dom.xpath('//h3[@class="thread_title"]/a/@href')


sub_pages = []
for sub_url in sub_urls:
    print(base_url + sub_url)
    for i in range(1, 11):
        sub_page = (base_url + sub_url).rstrip('.html') + '/' + str(i) + '.html'
        sub_pages.append(sub_page)

        #不要刷太多页（否则会被检测到立马封ip），或者获取优化获取策略防屏蔽
        sub_res = requests.get(sub_pages[0], headers=header)
        sub_res.encoding = 'utf-8'
        sub_dom = etree.HTML(sub_res.text)
        ips = sub_dom.xpath('//tbody/tr/td[1]/text()')
        ports = sub_dom.xpath('//tbody/tr/td[2]/text()')
        proxies_list = []
        for ip, port in zip(ips, ports):
            proxies = {}
            http = 'http://' + ip + ':' + port
            https = 'https://' + ip + ':' + port
            proxies['http'] = http
            proxies['https'] = https
            proxies_list.append(proxies)

        print(proxies_list)
