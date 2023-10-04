# -*- coding: utf-8 -*-
import requests
from loguru import logger
import json

class Spdier_data():

    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://cs.fang.lianjia.com/loupan/pg2/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": "^\\^",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^"
        }

    def http(self,url,params):
        res = requests.get(url,params=params,headers=self.headers)
        if res.status_code == 200:
            return res

    def get_data(self,url,params):
        response = self.http(url=url,params=params)
        items  = response.json()
        lists = items.get('data').get('list')
        for i in lists:
            item = {}
            item['address'] = i.get('address')
            item['city_name'] = i.get('city_name')
            item['decoration'] = i.get('decoration')
            item['district'] = i.get('district')
            item['title'] = i.get('title')
            item['show_price_info'] = i.get('show_price_info')
            logger.info(json.dumps(item))
            self.save_data(item)


    def save_data(self,data):
        with open('data.json','a',encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.write(',')

    def run(self):
        for i in range(1,3):
            url = "https://cs.fang.lianjia.com/loupan/pg{}/".format(str(i))
            params = {
                "_t": "1"
            }
            self.get_data(url,params)

if __name__ == '__main__':
    Spdier_data().run()