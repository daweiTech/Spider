# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 9:30
# @Author  : 4v1d
# @File    : 代理测试5.py
# @Software: PyCharm

from selenium import webdriver
import time,random
from pymongo import MongoClient
from selenium.webdriver.common.by import By




# options = webdriver.ChromeOptions()
# options.add_argument('--disable-blink-features=AutomationControlled')
# browser = webdriver.Chrome(chrome_options=options)
# browser.get('https://proxyhub.me/zh/gr-http-proxy-list.html')
# browser.implicitly_wait(10)
#
# button = browser.find_elements_by_css_selector('#main > div > div.filter > div > div:nth-child(1) > select > option:nth-child(3)')
# browser.execute_script("$(arguments[0]).click()", button)
import requests
from lxml import html
etree = html.etree
header = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'}
url = 'https://proxyhub.me/zh/cn-http-proxy-list.html'
res = requests.get(url,headers=header)
res.encoding = 'utf-8'
html = etree.HTML(res.text)
lis = html.xpath('//div[@class="list table-responsive"]//tr')

for i in lis[1:]:
    ips = i.xpath('./td[1]/text()')
    ports = i.xpath('./td[2]/text()')
    for ip, port in zip(ips, ports):
        print(ip+':'+port)
        # proxies = {}
        # http = 'http://' + ip + ':' + port
        # https = 'https://' + ip + ':' + port
        # proxies['http'] = http
        # proxies['https'] = https
        # proxies_list.append(proxies)
