# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 14:48
# @Author  : 4v1d
# @File    : mains.py
# @Software: PyCharm

from flask import Flask,render_template,jsonify

app = Flask(__name__)

# 路由，简称API
@app.route('/')
def index():
    item = []
    for i in range(1,9):
        data = {
            'id':1,
            'name':'张三',
            'age':3,
            'gw':'爬虫',
            'xz':'18k'
        }
        item.append(data)
    content = {
        'data':item,
        'status':0
    }
    return render_template('index.html',data=content)

@app.route('/api')
def index1():
    item = []
    for i in range(1,9):
        data = {
            'id':1,
            'name':'张三',
            'age':3,
            'gw':'爬虫',
            'xz':'18k'
        }
        item.append(data)
    content = {
        'data':item,
        'status':0
    }
    return jsonify(data=content)


if __name__ == '__main__':
    app.run()
