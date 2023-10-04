# -*- coding: utf-8 -*-
# @Time    : 2022/8/23 18:44
# @Author  : 4v1d
# @File    : 美食网.py
# @Software: PyCharm
import execjs

r = open('美食网.js',encoding='utf-8').read()
source = execjs.compile(r).call('pp')
print(source)