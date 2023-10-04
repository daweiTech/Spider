# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 8:54
# @Author  : 4v1d
# @File    : selenium过滑块.py
# @Software: PyCharm
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from loguru import logger
from selenium.webdriver.common.action_chains import ActionChains



username = '19859891007'
password = '1222David'


chromeOptions = webdriver.ChromeOptions()


chrome_browser = webdriver.Chrome(chrome_options=chromeOptions)
# 设置为开发者模式，防止网站识别
chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_browser = webdriver.Chrome()
# 通过浏览器的dev_tool在get页面将.webdriver属性改为"undefined"
chrome_browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
})
chrome_browser.implicitly_wait(10)
url = 'https://login.taobao.com/'
chrome_browser.get(url)
chrome_browser.maximize_window()
time.sleep(1)
js = "window.navigator.webdriver=false"
chrome_browser.execute_script(js)
time.sleep(2)
chrome_browser.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(username)
chrome_browser.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(password)
chrome_browser.find_element_by_xpath('//button[@type="submit"]').click()
try:
    # 切换框架
    chrome_browser.switch_to.frame("baxia-dialog-content")
    # 定位到滑块按钮元素
    ele_button = chrome_browser.find_elements(By.XPATH, "//span[@id='nc_1_n1z']")[-1]
    # 定位到滑块区域元素
    ele = chrome_browser.find_elements(By.XPATH, "//span[contains(text(), '最右边')]")[-1]
    # 拖动滑块
    ActionChains(chrome_browser).drag_and_drop_by_offset(ele_button, ele.size['width']/2,
    ele.size['height']).perform()
    time.sleep(1)
    ActionChains(chrome_browser).drag_and_drop_by_offset(ele_button, ele.size['width'], ele.size['height']).perform()
    time.sleep(2)
except:
    logger.info(f"没有滑块验证")

logger.info("登录成功...")