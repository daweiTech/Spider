# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 16:50
# @Author  : 4v1d
# @File    : 02-封装例子.py
# @Software: PyCharm

"""
声明一个电脑类：
属性：品牌、颜色、内存大小(写成封装)
写一个方法接口严格的控制查看属性
写一个方法接口严格的控制修改属性
"""
class Computer:
    def __init__(self,brand,color,memory_Size):
        self.__brand = brand
        self.__color = color
        self.__memory_Size = memory_Size

    def get_info(self):
        print("电脑牌子是{}，颜色是{}，内存大小是{}GB".format(self.__brand,self.__color,self.__memory_Size))

    def update_info(self,brand,color,memory_Size):
        if brand is not None:
            if type(brand) is not str:
                print("品牌需要输入字符串")
            else:
                self.__brand = brand
        if color is not None:
            if type(color) is not str:
                print("颜色需要输入字符串")
            else:
                self.__color = color
        if memory_Size is not None:
            if type(memory_Size) is not int:
                print("内存需要输入数字")
            else:
                self.__memory_Size = memory_Size
c = Computer('华为','灰色',8)
c.get_info()
c.update_info(1,1,16)
c.update_info('荣耀','黑色',16)
c.get_info()