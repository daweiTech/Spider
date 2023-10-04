





import requests
from lxml import html
etree = html.etree
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import pymongo
import time



options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(options=options)
browser.get('https://category.vip.com/suggest.php?keyword=%E5%8F%A3%E7%BA%A2&ff=235|12|1|1')
time.sleep(6)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 向下拉动一屏


html=etree.HTML(browser.page_source)
div_list=html.xpath('//section[@class="goods-list c-goods-list--normal"]/div')[1:]
for div in div_list:
   time.sleep(0.5)
   dic={}
   try:
       dic["title"]=div.xpath('.//div[@class="c-goods-item__name  c-goods-item__name--two-line"]/text()')[0]
       print(dic["title"])
   except:
       dic["title"]=""
