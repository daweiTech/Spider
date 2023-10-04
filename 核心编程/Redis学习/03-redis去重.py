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
        self.url = 'https://36kr.com/information/web_news/latest/'
        self.maps = lambda x:x if x else x

    def crawl(self):
        res = self.fetch(self.url)
        html = etree.HTML(res.text)
        obj = html.xpath('//p[@class="title-wrapper ellipsis-2"]/a/text()')
        for i in obj:
            title = self.maps(i)
            tag = client.sadd('david',title)
            if tag:
                logger.info('可以入库 {}'.format(title))
            else:
                logger.info('休息60秒钟')
                time.sleep(60)
                self.crawl()

if __name__ == '__main__':
    Crawl().crawl()