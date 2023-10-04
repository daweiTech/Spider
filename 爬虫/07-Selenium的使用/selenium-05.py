# -*- coding: utf-8 -*-
# @Time    : 2022/8/6 10:32
# @Author  : 4v1d
# @File    : selenium-04.py
# @Software: PyCharm
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
import random

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_argument('--disable-blink-features=AutomationControlled')
# with open('stealth.min.js') as f:
#     js = f.read()
# browser = webdriver.Chrome(options=options)
# browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": js
# })
# browser.get('https://category.vip.com/suggest.php?keyword=%E5%8F%A3%E7%BA%A2&ff=235%7C12%7C1%7C1&page=1')
# time.sleep(5)
#
#
#
# li = browser.find_elements(By.CLASS_NAME,"c-goods-item-bottom")
# li1 = browser.find_elements(By.CLASS_NAME,"c-goods-item__img")
# n = 0
# for i in li:
#     try:
#         title = i.find_element(By.XPATH, './/div[@class="c-goods-item__name  c-goods-item__name--one-line"]')
#         print(title.text)
#         n+=1
#     except:
#         pass
# print(len(li))
# print(n)
    # discount = i.find_element(By.XPATH,'.//div/div[@class="c-goods-item__discount  J-goods-item__discount"]')
    # print(discount.text)
    # price = i.find_element(By.XPATH, './/div/div[@class="c-goods-item__sale-price J-goods-item__sale-price"]')
    # print(price.text)
    # info = i.find_element(By.XPATH, './/div/div[@class="c-goods-item__price-tips  c-goods-item__price-tips--preheat"]')
    # print(info.text)
    # store = i.find_element(By.XPATH,'..//ul/li/span[@class="c-goods-item__pms-label c-goods-item__pms-label--haitao"]')
    # print(store.text)
    # product_url = i.find_element(By.XPATH,'..').get_attribute('href')
    # print(product_url)
    # img_url = i.find_element(By.XPATH, '..//img').get_attribute('src')
    # print(img_url)

#
#
#
#
#
#     break
# for j in li1:
#     url = j.find_element(By.XPATH,'./img').get_attribute('src')
#     print(url)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
with open('stealth.min.js') as f:
    js = f.read()

driver_path = r'F:\Python-项目\weixing\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})

time.sleep(2)
driver.get('http://www.customs.gov.cn/customs/302427/302442/3495580/index.html')