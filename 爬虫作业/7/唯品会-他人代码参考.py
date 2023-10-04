# -*- coding: utf-8 -*-
# @Time    : 2022/8/6 20:25
# @Author  : 4v1d
# @File    : 实战.py
# @Software: PyCharm

from selenium import webdriver
import time,random
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WpShop():

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument("-headless")#无头模式
        self.browser = webdriver.Chrome(chrome_options=options)
        client = MongoClient()  # 建立连接
        self.col = client['Spiders']['手机']
        self.rule = {
            'title':".//div[contains(@class,'c-goods-item__name')]",
            'discount':".//div[contains(@class,'c-goods-item__discount')]",
            'market_price':".//div[contains(@class,'c-goods-item__market-price')]",
            'sale_price':".//div[contains(@class,'c-goods-item__sale-price')]",
            'tips':".//div[contains(@class,'c-goods-item__price-tips')]",
            'next_page':"//a[@class='cat-paging-next next']"
        }

    def base(self):
        self.browser.get('https://www.vip.com/')
        time.sleep(5)
        input = self.browser.find_element(By.XPATH,'//input[contains(@class,"J-search")]')
        input.send_keys('手机')
        button = self.browser.find_element(By.XPATH,'//a[contains(@class,"c-search-button")]/span[last()]')
        self.browser.execute_script("$(arguments[0]).click()", button)
        # input.send_keys(Keys.ENTER)

    def spider(self):
        time.sleep(5)
        self.drop_down()
        li = self.browser.find_elements(By.CLASS_NAME,'c-goods-item')
        #print(li)
        for j in li:
            try:
                title = j.find_element(By.XPATH,self.rule['title'])
                discount = j.find_element(By.XPATH,self.rule['discount'])
                market_price = j.find_element(By.XPATH,self.rule['market_price'])
                sale_price = j.find_element(By.XPATH,self.rule['sale_price'])
                #tips = j.find_element(By.XPATH,self.rule['tips'])

                items = {
                    '标题': title.text,
                    '折扣': discount.text if discount else "",
                    "优惠价": sale_price.text if market_price else "",
                    "市场价": market_price.text if sale_price else ""
                    # "信息": tips.text
                }
                self.save_mongo(items)
            except Exception as e:
                print(e)
        self.page_next()

    def save_mongo(self,data):
        print(data)
        if isinstance(data, dict):
            res = self.col.insert_one(data)
            return res
        else:
            return '单条数据必须是这种格式：{"name":"age"}，你传入的是%s' % type(data)

    def page_next(self):
        try:
            next = self.browser.find_element(By.XPATH,self.rule['next_page'])
            if next:
                self.browser.execute_script("$(arguments[0]).click()",next)
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
    f = WpShop()
    f.base()
    f.spider()
