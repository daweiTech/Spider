# -*- coding: utf-8 -*-
# @Time    : 2022/7/29 16:26
# @Author  : 4v1d
# @File    : json格式.py
# @Software: PyCharm

"""
1.列表、字典、字符、数值、布尔
2.使用os模块
import os
os.remove("demofile.txt")
3.
import os

def scanfile(path):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            scanfile(filepath)
        print(filepath)

allfile = scanfile('自定义指定路径')

4.os.path.isfile()
5.os.path.isdir()
6.
import random
L = [1,2,4]
L1 = random.sample(L,2)
print(L1)
7.
import os, sys

# 列出目录
print ("目录为: %s"%os.listdir(os.getcwd()))

# 重命名
os.rename("1.txt","2.txt")

print ("重命名成功。")
8.
import os

print (os.getcwd())#获得当前目录
print (os.path.abspath('..'))#获得当前工作目录的父目录
9.
import json

data = { "name": "nanbei", "age": 18, "feature" : ["白", "富", "美"] }

with open('1.json','w',encoding='utf-8') as f:
    json.dump(data,f, indent=2, sort_keys=True, ensure_ascii=False)

with open('1.json','r',encoding='utf-8') as f1:
    result = json.loads(f1.read())
    print(result['feature'][-1])
"""
