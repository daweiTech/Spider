# -*- coding: utf-8 -*-
# @Time    : 2022/7/27 15:24
# @Author  : 4v1d
# @File    : 面向对象进阶题目解题.py
# @Software: PyCharm
"""
1.BD
2.
1 1 1
1 2 1
1 3 1
3.
        1.对象是具体存在的事物,而类则一个抽象的概念
        2.站在不同的角度总结出的类与对象是不同的
4.继承与被继承
5.C
6.B
7.B
8.
class Box:

    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height

    def Volume(self):
        return self.length * self.width * self.height

    def Surface_Area(self):
        return 2* (self.height*self.width+self.height*self.length
                   +self.width*self.length)
b = Box(2,3,4)
print(b.Volume())
print(b.Surface_Area())
9.
class Person:
    count = 0
    def __init__(self):
        Person.count += 1

p1 = Person()
p2 = Person()
p3 = Person()
print(Person.count)

class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def Area(self):
        area = self.width * self.length
        return '面积是%s'%area

class Square(Rectangle):

    def __init__(self,length,width):
        super().__init__(length,width)
        print(self.length,self.width)

    def __call__(self):

        if self.length!=self.width:
            print("不是正方形！")
            print('矩形的长是{},宽是{}'.format(self.length,self.width))
        else:
            print('正方形的边长是{}'.format(self.length))

    def __str__(self):
        return super().Area()

a = Square(2,2)
print(a)
a()
b = Square(10,3)
print(b)
b()

"""

import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test
collection = db['students']  # 都可以

import httpx

def get_data():
    res = httpx.get('https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1647605552864&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=2&pageSize=10&language=zh-cn&area=cn')
    # 数据变字典格式
    items = res.json()
    item = items.get('Data')['Posts']  # 列表形式
    for i in item:
        if isinstance(i,dict):
            collection.insert_one(i)
#get_data()

for i in collection.find():
    print(i)