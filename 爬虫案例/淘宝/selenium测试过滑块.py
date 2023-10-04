# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 9:18
# @Author  : 4v1d
# @File    : selenium测试过滑块.py
# @Software: PyCharm

from selenium import webdriver
import time,random
from pymongo import MongoClient
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
#options.add_argument("-headless")  # 无头模式
browser = webdriver.Chrome(chrome_options=options)
url = 'https://login.taobao.com/'
browser.get(url)
browser.maximize_window()