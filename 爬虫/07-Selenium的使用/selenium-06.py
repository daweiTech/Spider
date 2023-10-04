# -*- coding: utf-8 -*-
# @Author  : 夏洛
# @File    : 实战.py
# @VX : tl210329


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
        self.browser.get('https://category.vip.com/suggest.php?keyword=%E5%8F%A3%E7%BA%A2')
        time.sleep(5)

    def spider(self):
        self.drop_down()
        li = self.browser.find_elements(By.CLASS_NAME,"c-goods-item-bottom")
        for i in li:
            try:
                title = i.find_element(By.XPATH, './/div[@class="c-goods-item__name  c-goods-item__name--one-line"]')
            except:
                pass
            try:
                discount = i.find_element(By.XPATH, './/div[@class="c-goods-item__discount  J-goods-item__discount"]')
            except:
                pass
            try:
                price = i.find_element(By.XPATH, './/div[@class="c-goods-item__sale-price J-goods-item__sale-price"]')
            except:
                pass
            try:
                info = i.find_element(By.XPATH,
                                      './/div[@class="c-goods-item__price-tips  c-goods-item__price-tips--preheat"]')
            except:
                pass
            try:
                store = i.find_element(By.XPATH,
                                       '..//ul/li/span[@class="c-goods-item__pms-label c-goods-item__pms-label--haitao"]')
            except:
                pass
            try:
                product_url = i.find_element(By.XPATH, '..').get_attribute('href')
            except:
                pass
            img_url = i.find_element(By.XPATH, '..//img').get_attribute('src')
            items = {
                '名称': title.text,
                '折扣': discount.text,
                "价钱": price.text,
                '信息': info.text,
                '来源': store.text,
                '商品链接': product_url,
                '图片链接': img_url
            }
            self.save_mongo(items)
        #self.page_next()

    def save_mongo(self,data):
        print(data)
        client = MongoClient()  # 建立连接
        col = client['Spiders']['2']
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
            time.sleep(random.randint(400, 800) / 1000)

if __name__ == '__main__':
    f = YwShop()
    f.base()
    f.spider()
