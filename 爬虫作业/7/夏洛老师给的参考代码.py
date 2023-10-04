# encoding: utf-8
"""
@author: 夏洛
@QQ: 1972386194
@file: wph_data.py
"""


'''
抓取 口红信息

品牌名字提取
标题 价格 原价 折扣 品牌
翻页
入库  
'''

import requests
from lxml import etree
from loguru import logger
import pandas as pd
import asyncio
from pyppeteer import launch


class Wph(object):

    def __init__(self,url,name):
        self.url = url

        self.name = name

        self.headers = {
            'user-agent':'asdasdasdasdasdas'
        }

        self.session = requests.session() #全部都用    session 给请求头排序

        self.hadlnone = lambda x: x[0] if x else ''

    async def main(self,url):
        global browser
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        text = await page.content()  # 返回页面html
        return text

    def spider(self):
        '''
        处理业务逻辑的
        :return:
        '''
        df = pd.DataFrame(columns=['品牌', '标题', '原价', '现价', '折扣'])

        res = self.session.get(self.url, params={'keyword': self.name}, headers=self.headers, verify=False)
        html = etree.HTML(res.text)
        url_list = html.xpath('//div[@class="c-filter-group-content"]/div[contains(@class,"c-filter-group-scroll-brand")]/ul/li/a/@href')

        for i in url_list[1:4]:
            # 通过自动化加载地址 获取有数据的HTML
            page_html = asyncio.get_event_loop().run_until_complete(self.main('http:' + i))
            page = etree.HTML(page_html)
            htmls = page.xpath('//section[@id="J_searchCatList"]/div')
            for h in htmls[1:]:
                # 评判
                pingpai = self.hadlnone(h.xpath('//div[contains(@class,"c-breadcrumbs-cell-title")]/span/text()'))
                # pingpai =h.xpath('//div[contains(@class,"c-breadcrumbs-cell-title")]/span/text()')[0]
                # 标题
                title = self.hadlnone(h.xpath('.//div[contains(@class,"c-goods-item__name")]/text()'))
                # 价格  原价
                y_price = self.hadlnone(h.xpath('.//div[contains(@class,"c-goods-item__market-price")]/text()'))
                # 卖价
                x_price = self.hadlnone(h.xpath('.//div[contains(@class,"c-goods-item__sale-price")]/text()'))
                # 折扣
                zk = self.hadlnone(h.xpath('.//div[contains(@class,"c-goods-item__discount")]/text()'))

                logger.info(f'品牌{pingpai}，标题{title}，原价{y_price}，现价{x_price}，折扣{zk}')
                # 构造字典
                pro = {
                    '品牌': pingpai,
                    '标题': title,
                    '原价': y_price,
                    '现价': x_price,
                    '折扣': zk
                }
                df = df.append([pro])
        df.to_excel('唯品会数据2.xlsx', index=False)


if __name__ == '__main__':
    url = 'https://category.vip.com/suggest.php'
    name = "口红"
    w = Wph(url,name)
    w.spider()



