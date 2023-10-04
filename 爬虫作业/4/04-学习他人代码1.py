# -*- coding: utf-8 -*-
# @Time    : 2022/7/30 14:27
# @Author  : 4v1d
# @File    : 04-学习他人代码1.py
# @Software: PyCharm
from urllib.parse import urljoin

import pymongo
import pymysql
from lxml import html
etree = html.etree

from bases import *


client = pymongo.MongoClient('127.0.0.1', port=27017)
db = client.spiders
collection = db.fang_ke

db = pymysql.connect(host='127.0.0.1', user='root', password='root', port=3306, db='xyc')
cursor = db.cursor()  # 游标


def get_datas():
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
        print(item)
        #save_mongo(item)
        t = tuple(item.values())
        data_li.append(t)
    print(data_li)
    #save_mysql(data_li)


def save_mongo(data):
    if isinstance(data, dict):
        collection.insert(data)


def save_mysql(datas):
    for data in datas:
        sql = 'INSERT INTO fang_ke (detail_url,title,location,resblock_room,area,main_price,total_price,resblock_tag,resblock_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            if cursor.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])):
                print('Successful')
                db.commit()
        except Exception as e:
            print('Failed')
            db.rollback()
    db.close()


if __name__ == '__main__':
    get_datas()