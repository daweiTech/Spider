# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 14:03
# @Author  : 4v1d
# @File    : test.py
# @Software: PyCharm
# *coding:utf-8 *.
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的Chrome浏览器创建浏览器对象
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
with open('stealth.min.js') as f:
    js = f.read()

driver_path = r'F:\Python-项目\weixing\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path,chrome_options = options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})

# get 方法会一直等到页面被完全加载，才会继续程序
time.sleep(2)
driver.get('https://music.163.com/user/home?id=1355997463')

