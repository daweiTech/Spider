# -*- coding: utf-8 -*-
# @Time    : 2022/8/20 14:58
# @Author  : 4v1d
# @File    : 数据去重算法.py
# @Software: PyCharm
'''
redis 去重 集合类型
布隆算法

2种方式
    URL去重   针对采集的地址
    data去重  针对某一个数据

    redis  默认会进行encode 编码  获取数据要解码 decode
'''
from bases import Spiders
from lxml import html
import time
import redis
import pymongo
import hashlib
etree = html.etree
from loguru import logger
import pymysql
from dbutils.pooled_db import PooledDB


# client = pymongo.MongoClient('127.0.0.1', port=27017)
# db = client.Spiders
# collection = db['36kr']




class Crawl(Spiders):

    def __init__(self):
        self.url = 'https://36kr.com/information/web_news/latest/'
        self.client = redis.Redis()
        self.maps = lambda x: x[0] if x else x
        POOL = PooledDB(
            creator=pymysql,
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',  # 输入数据库密码
            database='test',  # 数据库名
            charset='utf8'
        )
        self.conn = POOL.connection()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql_createdb = """
        CREATE TABLE IF NOT EXISTS `36Kr`(
                         id INT NOT NULL AUTO_INCREMENT,
                         `标题`  CHAR(100),
                         `作者` CHAR(10),
                         `摘要` CHAR(100),
                         `详情链接` CHAR(100),
                         `时间` CHAR(10),
                         PRIMARY KEY(id)
                         ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
        self.cursor.execute(sql_createdb)

    def ma5_data(self, content):
        m = hashlib.md5()
        m.update(content.encode())
        return m.hexdigest()

    def save_mysql(self,dict):
        sql_insert = "insert IGNORE INTO 36Kr( `标题`, `作者`, `摘要`, `详情链接`,`时间`) values(\"%s\",\"%s\",\"%s\"," \
                     "\"%s\",\"%s\")" % (
                     str(dict['标题']), str(dict['作者']), str(dict['摘要']), str(dict['详情链接']), str(dict['时间']))
        self.cursor.execute(sql_insert)
        self.conn.commit()


    def crawl(self):
        res = self.fetch(self.url)
        html = etree.HTML(res.text)
        obj = html.xpath('//div[@class="information-flow-list"]/div')
        for i in obj:
            title = self.maps(i.xpath('.//p[@class="title-wrapper ellipsis-2"]/a/text()'))
            # print(title)
            xxx = self.ma5_data(title)  # 对数据进行压缩  减少内存损耗
            tag = self.client.sadd('36kr', xxx)  # 返回值 0 1
            base_url = 'https://36kr.com'
            # 表示数据可以继续爬  对数据进行入库   logger = print
            detail_url = self.maps(i.xpath('.//p['
                                           '@class="title-wrapper '
                                           'ellipsis-2"]/a/@href'))
            print(detail_url)
            url = base_url + detail_url
            print(url)
            source = self.maps(
                i.xpath('.//div[@class="kr-flow-bar"]/a/text()'))
            digst = self.maps(i.xpath('.//div[@class="article-item-info clearfloat"]/a/text()'))
            update_time = self.maps(i.xpath('.//div[@class="kr-flow-bar"]/span[2]/text()'))
            item = {
                '标题': title,
                '作者': source,
                '摘要': digst,
                '详情链接': url,
                '时间': update_time
            }
            # logger.info('可以入库   {}'.format(title))



    def save(self, data):
        with open('data.txt', 'a', encoding='utf-8') as x:
            x.write(data)
            x.write('\r\n')

    def run(self):
        while True:
            logger.info('开始启动爬虫')
            self.crawl()


if __name__ == '__main__':
    Crawl().run()