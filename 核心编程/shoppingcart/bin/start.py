#启动程序配置路径 bin/start.py

from json.tool import main
import sys
import os

#print(os.path.dirname(__file__))
#拿到当前执行的项目目录
Source_path = os.path.dirname(os.path.dirname(__file__))

sys.path.append(Source_path)
# print(sys.path)
"""
['e:\\图灵Python学习\\shoppingcart\\bin', 'F:\\Python-项目\\python3.6\\python36.zip', 'F:\\Python-项目
\\python3.6\\DLLs', 'F:\\Python-项目\\python3.6\\lib', 'F:\\Python-项目\\python3.6', 'C:\\Users\\David\\AppData\\Roaming\\Python\\Python36\\site-packages', 'F:\\Python-项目\\python3.6\\lib\\site-packages', 'F:\\Python-项目\\python3.6\\lib\\site-packages\\pip-22.1.2-py3.6.egg', 'e:/图灵Python学习/shoppingcart']
"""

#启动core/src.py 文件run函数

from core import src

if __name__ == '__main__':
    src.run()