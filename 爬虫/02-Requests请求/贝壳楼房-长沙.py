# encoding: utf-8
import requests
from loguru import logger
import json
import pymysql
import pymongo

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
        print(type(response))
        items  = response.json()
        lists = items.get('data').get('list')
        self.datalist = []
        for i in lists:
            item = {}
            item['address'] = i.get('address')
            item['city_name'] = i.get('city_name')
            item['decoration'] = i.get('decoration')
            item['district'] = i.get('district')
            item['title'] = i.get('title')
            item['show_price_info'] = i.get('show_price_info')
            self.datalist.append(item)
            #logger.info(json.dumps(item))
            #self.save_data(item)
            self.save_data1()
        print(self.datalist)


    def save_data(self,data):
        with open('data.json','a',encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.write(',')

    def run(self):
        for i in range(1,3):
            url = "https://cs.fang.ke.com/loupan/pg{}/".format(str(i))
            params = {
                "_t": "1"
            }
            self.get_data(url,params)

    def generate_sql(self,data_list):
        data = data_list[0]
        cols = ", ".join('`{}`'.format(k) for k in data.keys())
        val_cols = ', '.join('%({})s'.format(k) for k in data.keys())
        sql = """
        INSERT INTO information(%s) VALUES(%s)
        """ % (cols, val_cols)
        return sql

    def save_data1(self):
        MYSQL_CONFIG = {
            'host': 'localhost',  # IP地址
            'port': 3306,  # 端口
            'user': 'root',  # 用户名
            'passwd': 'root',  # 密码
            'db': 'xyc',  # 数据库
            'charset': 'utf8',  # 编码
        }
        db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='xyc')
        cursor = db.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS information ' \
              '(id VARCHAR(255) NOT NULL, ' \
              'address VARCHAR(255) NOT NULL, ' \
              'city_name VARCHAR(255) NOT NULL, ' \
              'decoration VARCHAR(255) NOT NULL,' \
              'district VARCHAR(255) NOT NULL,' \
              'title  VARCHAR(255) NOT NULL,' \
              'show_price_info VARCHAR(255) NOT NULL,' \
              'PRIMARY KEY (id))'
        cursor.execute(sql)
        db.close()

        conn = pymysql.connect(**MYSQL_CONFIG)  # 数据库连接
        cur = conn.cursor()  # 游标对象

        sql = self.generate_sql(self.datalist)
        cur.executemany(sql, self.datalist)
        conn.commit()
        conn.rollback()
        cur.close()
        conn.close()
if __name__ == '__main__':
    Spdier_data().run()