# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 16:33
# @Author  : 4v1d
# @File    : 01-学习封装.py
# @Software: PyCharm

class Demo:
    __x = 1
    __y = 2

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def func(self):
        print('func')

    def get_info(self):
        print(self.__x,self.__y,self.name,self.age)
        self.func()

# print(Demo.__name__)
# print(Demo.x)
# print(Demo.y)
# d = Demo('david',18)
# d.get_info()
"""
封装：将属性变为私有（注意Python只是进行隐藏，并没有像Java一样严格做到不能访问），
使得类外不能访问数据，数据被隐藏起来了；
这样就需要接口来代替我们进行数据的访问了
"""

class People:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print('name:%s age:%s'%(self.__name,self.__age))

    def set_info(self, name, age):
        if type(name) is not str:
            print('名字必须为字符串')
            return
        if type(age) is not int:
            print('年龄必须为数字')
            return
        self.__name= name
        self.__age = age

p = People('夏洛',18)
p.tell_info()
p.__name = '大海'#只是添加了一个属性
p.tell_info()
print(p.__name)
print(p.__dict__)#通过前面得到{'_People__name': '夏洛', '_People__age': 18, '__name': '大海'}
p._People__age = 20
p.tell_info()