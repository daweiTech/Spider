# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 16:22
# @Author  : 4v1d
# @File    : 03-redis去重.py
# @Software: PyCharm
import time

import redis

from bases import *
from lxml import html
etree = html.etree
client = redis.Redis()
from loguru import logger

class Crawl(Spiders):

    def __init__(self):
        self.url = 'https://s.weibo.com/top/summary/?sudaref=cn.bing.com'
        self.maps = lambda x:x if x else x

    def crawl(self):
        res = self.fetch(self.url)
        res.encoding = 'GBK'
        r = res.text
        print(r)
        html = etree.HTML(r)
        obj = html.xpath('//td[@class="td-02"]/a')
        print(obj)
        for i in obj:
            title = self.maps(i)
            tag = client.sadd('jack',title)
            if tag:
                logger.info('可以入库 {}'.format(title))
            else:
                logger.info('休息60秒钟')
                time.sleep(60)
                self.crawl()

if __name__ == '__main__':
    Crawl().crawl()