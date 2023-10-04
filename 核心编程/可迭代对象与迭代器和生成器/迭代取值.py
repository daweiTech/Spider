# -*- coding: utf-8 -*-
# @Time    : 2022/7/10 10:25
# @Author  : 4v1d
# @File    : 迭代取值.py
# @Software: PyCharm

#哪些数据类型需要迭代
#字符串、列表、元组、字典、集合、文件等等

#__iter__方法，能够使用这个方法都是可迭代对象
#如果可迭代对象可使用next方法，那就成为迭代器
a = 1
c = 'hello'
C = c.__iter__()
print(C)#变成迭代器，<str_iterator object at 0x00000261E1C78910>

f = open('1.txt','rt')
print(f.__iter__().__next__())
#既有iter内置方法，又有next方法，所以文件是迭代器
#自然可迭代对象使用了iter内置方法变成迭代器后，就可以使用next方法了

dic = {'x':1,'y':2}
iter_dic = dic.__iter__()
print(iter_dic)
print(iter_dic.__next__())
print(iter_dic.__next__())
#next最大步数由数据个数决定，这边2次就到头了。

l = [1,2,3]

print(l.__iter__().__next__())
print(l.__iter__().__next__())
print(l.__iter__().__next__())
print(l.__iter__().__next__())
#不报错，因为每次都是取新的


#for循环直接对迭代器进行取值

f = open('1.txt','r')
for i in f.__iter__():
    print(i)
