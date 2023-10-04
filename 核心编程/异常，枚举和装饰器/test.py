# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 14:56
# @Author  : 4v1d
# @File    : script1.py
# @Software: PyCharm
#
# def run1():
#     return run1()
# res=run1()

# def run3():
#     return run1
#
# def run1():
#     def run2():
#         return run3()
#     return run2
# res=run1()()
# print(res)
# def func():
#     name = 'python'
#     def inner():
#         print(name)
#     return inner
#
# f = func()  # f = func() = inner
# f()  # f() = inner
# # 输出结果：python
#
# m = func
# m()

# def run1():
#     def run2():
#         pass
#     return run2()
# res=run1()
# print(res)
#
# def run1():
#     def run2():
#         pass
#     return run2
# res=run1()
# print(res)


def func(**kwargs):
    print(kwargs)
    a = sorted(kwargs)
    print(a)
    return ''.join(sorted(kwargs))

print(func(x=2, y=1, z=3))
print(''.join(sorted({'x': 2, 'y': 1, 'z': 3})))

def func(**kwargs):
    print(sorted(kwargs,key=lambda name:kwargs[name],reverse=False))
    return ''.join(sorted(kwargs,key=lambda name:kwargs[name],reverse=False))

print(func(x=2, y=1, z=3))


