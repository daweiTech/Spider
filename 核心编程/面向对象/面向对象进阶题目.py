# -*- coding: utf-8 -*-
# @Time    : 2022/7/27 15:24
# @Author  : 4v1d
# @File    : 面向对象进阶题目.py
# @Software: PyCharm

"""
第一题



关于 Python 类的继承正确的说法是?(多选)



A. Python 类无法继承



B. Python 类可以继承



C. 可以有多个父类



D. 只能有一个父类



第二题



以下代码输出是什么?请给出答案________



class Parent:



    x = 1



class Child1(Parent):



    pass



class Child2(Parent):



    pass



print(Parent.x, Child1.x, Child2.x)



Child1.x = 2



print(Parent.x, Child1.x, Child2.x)



Child1.x = 3



print(Parent.x, Child1.x, Child2.x)



第三题



类和对象的关系是_____



第四题



类和父类的关系是_____



第五题（单选题）



以下代码的输出结果是



class A:



    def __init__(self, i = 1):



        self.i = i



class B(A):



    def __init__(self, j = 2):



        super().__init__()



        self.j = j



b = B()



print(b.i,b.j)



A.0 1



B.0 0



C.1 2



D.0 2



第六题（单选题）



以下代码打印结果是



class A:



    def __init__(self, i = 0):



        self.i = i



    def m1(self):



        self.i += 1







class B(A):



    def __init__(self, j = 0):



        A.__init__(self, 3)



        self.j = j



    def m1(self):



        self.j += 1



b = B()



b.m1()



print(b.i, b.j)



A.2 0



B.3 1



C.4 0



D.3 0



第七题（单选题）



以下代码打印结果是



class A:



    def __init__(self):



        self.i = 1



    def m(self):



        self.i = 10



class B(A):



    def m(self):



        self.i += 1



        return self.i



b = B()



print(b.m())



 A. 1



 B. 2



 C. 10



 D. 0



第八题



设计一个立方体类（Box），定义三个属性，分别是长、宽、高。定义两个方法，分别计算并输出立方体的体积和表面积



选做



第九题



创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数



第十题



定义一个矩形类，有长和宽两个实例/对象属性， 还有一个计算面积的方法；
定义正方形类(继承矩形类)，实现类的实例/对象可调用，调用时打印正方形的边长(是矩形就打印不是正方形)；
同时，直接打印类实例时能够打印出实例的面积，打印的这个面积会使用父类的方法。
"""
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def get_area(self):
        area = self.length * self.width
        return '面积是%s'% area
class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)

    def __call__(self):
        if self.length != self.width:
            print('不是正方形')
            print('矩形长是%s,宽是%s'%(self.length,self.width))
        else:
            print('正方形的边长%s'%self.width)
    def __str__(self):
        return super().get_area()
s=Square(40,41)
print(s)
s()