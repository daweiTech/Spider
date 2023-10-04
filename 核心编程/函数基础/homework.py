# -*- coding: utf-8 -*-
# @Time    : 2022/7/11 10:16
# @Author  : 4v1d
# @File    : homework.py
# @Software: PyCharm

#数字比大小，三个数

def compare_Num(x,y,z):
    while(z<y or z<x or x>y):
        if x > y:
            i = x
            x = y
            y = i
        if(y > z):
            j = y
            y = z
            z = j
    print(x,y,z)

compare_Num(10,9,7)



