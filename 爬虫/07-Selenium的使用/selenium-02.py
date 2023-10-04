"""
# -*- coding: utf-8 -*-
# @Time    : 2022/8/6 10:04
# @Author  : 4v1d
# @File    : selenium-02.py
# @Software: PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from selenium import webdriver
options = webdriver.ChromeOptions()

# 禁止图片
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

# 无头模式 在后台运行
# options.add_argument("-headless")

# 通过设置user-agent
user_ag='MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22;CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
options.add_argument('user-agent=%s'% user_ag)

#隐藏"Chrome正在受到自动软件的控制"
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])

#设置代理
# options.add_argument('proxy-server=' +'192.168.0.28:808')

# 初始化配置
browser = webdriver.Chrome(chrome_options=options)
browser.get('http://www.baidu.com')
#将浏览器最大化显示
browser.maximize_window()
# 设置宽高
browser.set_window_size(480, 800)

# 通过js新打开一个窗口
browser.execute_script('window.open("https://www.baidu.com");')

