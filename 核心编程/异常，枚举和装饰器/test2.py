# # -*- coding: utf-8 -*-
# # @Time    : 2022/7/18 15:48
# # @Author  : 4v1d
# # @File    : test2.py
# # @Software: PyCharm
#
# def login_verified(func):#
#     def decorate():
#         username = ''
#         password = ''
#         while True:
#             if username=='' or password=='':
#                 username = input("请输入账号：")
#                 password = input("请输入密码：")
#                 continue
#             else:
#                 return func()
#                 break
#     return decorate
#
# @login_verified
# def run():
#     print('开始执行函数')
#
# run()

def run_dahai():

    print('============')

    print('我是大海')

    print('============')

def decorate(func):

    def new_func(*args,**kwargs):

        print('我是被装饰函数前面的代码')

        func(*args,**kwargs)

        print('我是被装饰函数后面的代码')

    return new_func

new_func=decorate(run_dahai)

new_func()


def decorate(func):

    def new_func(*args,**kwargs):

        print('我是被装饰函数前面的代码')

        func(*args,**kwargs)

        print('我是被装饰函数后面的代码')

    return new_func

run_dahai=decorate(run_dahai)

run_dahai()