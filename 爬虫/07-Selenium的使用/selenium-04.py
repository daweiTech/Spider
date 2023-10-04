# -*- coding: utf-8 -*-
# @Time    : 2022/8/6 10:32
# @Author  : 4v1d
# @File    : selenium-04.py
# @Software: PyCharm
import time

from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
with open('stealth.min.js') as f:
    js = f.read()

browser = webdriver.Chrome(options=options)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})
browser.get('https://category.vip.com/suggest.php?keyword=%E5%8F%A3%E7%BA%A2&ff=235|12|1|1')
time.sleep(5)

# for x in range(1, 10):
#     j = x / 10
#     k = 0.00
#     for y in range(1, 11):
#         js = f"document.documentElement.scrollTop = document.documentElement.scrollHeight * {round((j + k), 2)}"
#         browser.execute_script(js)
#         # time.sleep(random.randint(400, 800) / 1000)
#         time.sleep(1)
#         k += 0.01
# import random
# for x in range(1, 10):
#     j = x / 10
#     js = f"document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}"
#     browser.execute_script(js)
#     time.sleep(random.randint(400, 800) / 1000)
#
# js1 = f"document.documentElement.scrollTop = document.documentElement.scrollHeight * -0.1"
js = 'var q=document.documentElement.scrollTop=8000'
browser.execute_script(js)
time.sleep(3)
js = 'var q=document.documentElement.scrollTop=8000'
browser.execute_script(js)
time.sleep(3)

i = 0
for j in range(2,122):
    try:
        title = browser.find_element_by_css_selector('#J_searchCatList > div:nth-child({}) > a > div.c-goods-item-bottom > div.c-goods-item__name.c-goods-item__name--one-line'.format(j))
        print(title.text)
        i+=1
    except:
        pass

print("success个数是{}".format(i))


#J_searchCatList > div:nth-child(3) > a > div.c-goods-item-bottom > div.c-goods-item__name.c-goods-item__name--one-line
#J_searchCatList > div:nth-child(121) > a > div.c-goods-item-bottom > div.c-goods-item__name.c-goods-item__name--one-line