# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 15:32
# @Author  : 4v1d
# @File    : script1.py
# @Software: PyCharm

str_1='d52a733i2327ha244i982d23s553b245'
l = []
for i in str_1:
    try:
        if i>='a' and i<'z':
            l.append(i)
        else:
            raise TypeError
    except Exception as e:
        pass
print(''.join(l))


def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

@debug
def hello():
    print("hello")

hello()