# -*- coding: utf-8 -*-
# @Time    : 2022/8/23 11:47
# @Author  : 4v1d
# @File    : 热门视频榜单.py
# @Software: PyCharm
from xl_utils import bases
from lxml import html
etree = html.etree


class Crawler:
    def __init__(self):
        self.rule = {
            'video_url':'./div[@class="content"]/div[@class="info"]/a/@href',
            'title':'./div[@class="content"]/div[@class="info"]/a/text()',
            'up_url':'./div[@class="content"]/div[@class="info"]/div/a/@href',
            'up':'./div[@class="content"]/div[@class="info"]/div/a/span/text()',
            'like':'./div[@class="content"]/div[@class="info"]/div['
                   '@class="detail"]/div[@class="detail-state"]/span[1]/text()',
            'barrage':'./div[@class="content"]/div[@class="info"]/div['
                      '@class="detail"]/div[@class="detail-state"]/span[2]/text()',
        }

    def run(self):
        r = bases.Spiders().fetch('https://www.bilibili.com/v/popular/rank/all')
        source = etree.HTML(r.text)
        video_list = source.xpath('//ul[@class="rank-list"]/li')
        for i in video_list:
            # up = i.xpath(self.rule['up'])[0].strip()
            item ={
                'up名字' : i.xpath(self.rule['up'])[0].strip(),
                'up主页链接' : 'https:' + i.xpath(self.rule['up_url'])[0],
                '视频名字' : i.xpath(self.rule['title'])[0],
                '视频链接' : 'https:' + i.xpath(self.rule['video_url'])[0],
                '点赞数' : i.xpath(self.rule['like'])[0].strip(),
                '弹幕数' : i.xpath(self.rule['barrage'])[0].strip(),
            }
            print(item)

if __name__ == '__main__':
    Crawler().run()

