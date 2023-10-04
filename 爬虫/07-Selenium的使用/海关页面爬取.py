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
        self.col = client['Spiders']['海关']


    def crawl(self):
        url = 'http://www.customs.gov.cn/customs/302427/302442/3495580/index.html'
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        iframe = self.browser.find_element_by_xpath('//*[@id="06f09e1efe1e4460a6655b27b4d0cd76"]/div[2]/div/iframe')
        self.browser.switch_to.frame(iframe)
        lis = self.browser.find_elements(By.ID,'//tr')
        for i in lis[5:]:
            id1 = i.find_element(By.XPATH,'//td[1]')
            name = i.find_element(By.XPATH,'//td[2]')
            id2 = i.find_element(By.XPATH,'//td[3]')
            info  = i.find_element(By.XPATH, '//td[4]')
            dict = {
                '相关编号':id1.text,
                '中文名称':name.text,
                '决定税号':id2.text,
                '规格型号':info.text
            }
            self.save_mongo(dict)

    def save_mongo(self, data):
        print(data)
        if isinstance(data, dict):
            res = self.col.insert_one(data)
            return res
        else:
            return '单条数据必须是这种格式：{"name":"age"}，你传入的是%s' % type(data)

        # name = self.browser.find_element_by_xpath('//*[@id="grid"]/div[2]/table/tbody/tr[1]/td[2]')
        # print(name.text)
        # id = self.browser.find_element_by_xpath('//*[@id="grid"]/div[2]/table/tbody/tr[1]/td[1]')
        # print(id.text)

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

if __name__ == '__main__':
    Spider().crawl