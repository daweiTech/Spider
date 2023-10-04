# -*- coding: utf-8 -*-
# @Time    : 2022/8/6 9:54
# @Author  : 4v1d
# @File    : selenium-01.py
# @Software: PyCharm
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# options.add_argument("-headless")
# 打开指定（chrome）浏览器
browser = webdriver.Chrome()
# 指定加载页面
browser.get("http://www.baidu.com/")
# 通过name属性选择文本框元素，并设置内容
browser.find_element(By.NAME,'wd').send_keys("李大为")
# 通过通过ID属性获取“百度一下”按钮，并执行点击操作
browser.find_element(By.ID,"su").click()
# 提取页面
print(browser.page_source.encode('utf-8'))
with open('1.html','wb') as f:
    f.write(browser.page_source.encode('utf-8'))

# 设置五秒后执行下一步
time.sleep(5)
# 关闭浏览器
browser.quit()