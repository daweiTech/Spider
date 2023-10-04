# -*- coding: utf-8 -*-
# @Time    : 2022/8/6 20:25
# @Author  : 4v1d
# @File    : 实战.py
# @Software: PyCharm

from selenium import webdriver
import time,random
from pymongo import MongoClient
from selenium.webdriver.common.by import By
class YwShop():

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.browser = webdriver.Chrome(chrome_options=options)

    def base(self):
        self.browser.get('http://www.yiwugo.com/')
        input = self.browser.find_element(By.ID,'inputkey')
        input.send_keys('饰品')
        self.browser.find_element(By.XPATH,'//div[@class="search-index"]/span[last()]').click()

    def spider(self):
        self.drop_down()
        li = self.browser.find_elements(By.CLASS_NAME,'pro_list_product_img2')
        print(li)
        for j in li:
            title = j.find_element(By.XPATH,'.//li/a[@class="productloc"]')
            price = j.find_element(By.XPATH,'.//li/span[@class="pri-left"]/em')
            info = j.find_elements(By.XPATH,'.//li/span[@class="pri-right"]/span')
            address = j.find_element(By.XPATH,'.//li[@class="shshopname"]')
            texts = ''
            for i in info:
                texts = i.text
            items = {
                '标题':title.text,
                "价钱": price.text,
                "地址": address.text,
                "信息":texts
            }
            self.save_mongo(items)
        self.page_next()

    def save_mongo(self,data):
        print(data)
        client = MongoClient()  # 建立连接
        col = client['Spiders']['义乌']
        if isinstance(data, dict):
            res = col.insert_one(data)
            return res
        else:
            return '单条数据必须是这种格式：{"name":"age"}，你传入的是%s' % type(data)

    def page_next(self):
        try:
            next = self.browser.find_element(By.XPATH,'//ul[@class="right"]/a[@class="page_next_yes"]')
            if next:
                next.click()
                self.spider()
            else:
                self.browser.close()
        except Exception as e:
            print(e)


    def drop_down(self):
        for x in range(1, 10):
            j = x / 10
            js = f"document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}"
            self.browser.execute_script(js)
            time.sleep(random.randint(400,800)/1000)

if __name__ == '__main__':
    f = YwShop()
    f.base()
    f.spider()
