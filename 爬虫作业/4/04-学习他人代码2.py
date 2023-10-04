# -*- coding: utf-8 -*-
# @Time    : 2022/7/30 14:35
# @Author  : 4v1d
# @File    : 测试04-学习他人代码.py
# @Software: PyCharm
from bases import *
from urllib.parse import urljoin
#
# url = 'https://cs.fang.ke.com/loupan/'
# response = Spiders().fetch(url)
# html = etree.HTML(response.text)
# datas = html.xpath("//ul[@class='resblock-list-wrapper']/li")
# print(datas)
# count = 0
# for data in datas:
#     #print(data)
#     detail_url = urljoin('https://cs.fang.ke.com/', (''.join(data.xpath("./a/@href"))))
#     print(detail_url)
#     title = ''.join(data.xpath("./a/@title"))
#     a = data.xpath(
#         './div[@class="resblock-desc-wrapper"]/div/div/div/div/span/text()')
#     print(a)
#


url = 'https://cs.fang.ke.com/loupan/'
response = Spiders().fetch(url)
html = etree.HTML(response.text)
datas = html.xpath("//ul[@class='resblock-list-wrapper']/li")
data_li = []
for data in datas:
    item = {}
    # 详情url
    item['detail_url'] = urljoin('https://cs.fang.ke.com/', (''.join(data.xpath("./a/@href"))))
    # 楼盘
    item['title'] = ''.join(data.xpath("./a/@title"))
    # 位置
    item['location'] = "".join(data.xpath("./div[@class='resblock-desc-wrapper']/a/@title"))
    # 户型
    item['resblock_room'] = "".join(
        data.xpath("./div[@class='resblock-desc-wrapper']/a[@class='resblock-room']/span[2]/text()"))
    # 建面
    item['area'] = "".join(
        data.xpath("./div[@class='resblock-desc-wrapper']/a[@class='resblock-room']/span[@class='area']/text()"))
    # 均价
    item['main_price'] = "".join(
        data.xpath("./div[@class='resblock-desc-wrapper']//div[@class='main-price']/span/text()"))
    # 总价
    item['total_price'] = "".join(data.xpath("./div[@class='resblock-desc-wrapper']//div[@class='second']/text()"))
    # 优势
    item['resblock_tag'] = ",".join(
        data.xpath("./div[@class='resblock-desc-wrapper']//div[@class='resblock-tag']/span/text()"))
    # 性质 （在售，住宅，商用）
    item['resblock_type'] = ",".join(
        data.xpath("./div[@class='resblock-desc-wrapper']//div[@class='resblock-name']/span/text()"))
    #print(item)
    # save_mongo(item)
    t = tuple(item.values())
    #print((item.values()))
    # print(t)
    for k in item.values():
        print(k)