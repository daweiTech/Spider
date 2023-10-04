# -*- coding: utf-8 -*-
# @Time    : 2022/8/13 16:02
# @Author  : 4v1d
# @File    : 海关页面爬取.py
# @Software: PyCharm


#导入库
import time
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor

class Spider:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # options.add_argument('--proxy-server=http://116.202.13.106:8080')
        with open('stealth.min.js') as f:
            js = f.read()

        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": js
        })
        time.sleep(2)
        client = MongoClient()  # 建立连接
        self.col = client['Spiders']['海关1']
        self.page = 0
        self.rule = {
            'one': '//a[@class="k-link k-pager-nav"]',
            'other': '//a[@class="k-link k-pager-nav"][2]'
        }
        url = 'http://gss.customs.gov.cn/clsouter2020/Home/ClassifyYCDSearch'
        self.browser.get(url)


    def crawl(self):
        self.browser.implicitly_wait(10)
        lis = self.browser.find_elements(By.XPATH,'//tr')
        for i in lis[6:]:
            id1 = i.find_element(By.XPATH,'./td[1]')
            name = i.find_element(By.XPATH,'./td[2]')
            id2 = i.find_element(By.XPATH,'./td[3]')
            info  = i.find_element(By.XPATH, './td[4]')
            dict = {
                '相关编号':id1.text,
                '中文名称':name.text,
                '决定税号':id2.text,
                '规格型号':info.text
            }
            self.save_mongo(dict)
        self.page+=1
        self.page_next()

    def save_mongo(self, data):
        print(data)
        if isinstance(data, dict):
            res = self.col.insert_one(data)
            return res
        else:
            return '单条数据必须是这种格式：{"name":"age"}，你传入的是%s' % type(data)

    def page_next(self):
        try:
            if self.page == 1:
                next_page = self.browser.find_element(By.XPATH, self.rule['one'])
                self.browser.execute_script("$(arguments[0]).click()", next_page)
                time.sleep(3)
                self.crawl()
            else:
                print("第{}页数据采集完毕".format(self.page-1))
                next_page = self.browser.find_element(By.XPATH, self.rule['other'])
                self.browser.execute_script("$(arguments[0]).click()", next_page)
                time.sleep(3)
                self.crawl()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    with ThreadPoolExecutor(100) as f:
            f.submit(Spider().crawl)
