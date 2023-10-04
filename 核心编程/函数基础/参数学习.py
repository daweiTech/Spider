# -*- coding: utf-8 -*-
# @Time    : 2022/7/11 10:01
# @Author  : 4v1d
# @File    : 参数学习.py
# @Software: PyCharm

def foo(x,y,*args,m,n,**kwargs):
    print(x,y)
    print(args)
    print(m,n)
    print(kwargs)

# foo(1,2,3,4,5,6,a=1,b=2,c=3),错误
#foo(1,2,3,4,5,6,m=100,n=200,a=1,b=2,c=3)

def factory(*args,**kwargs):
    print(args)#元组
    print(kwargs)#字典
factory()
# factory(1,2,3,4,a=5,b=6,c=7)
factory(1,2,3,3,nba='汤普森')


dic = {'name':'dahai','age':18}
print(*dic)