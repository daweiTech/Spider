# -*- coding: utf-8 -*-
# @Time    : 2022/7/20 15:53
# @Author  : 4v1d
# @File    : 01-redis命令.py
# @Software: PyCharm

"""
2. list类型 字符串列表

key         value（字符串）
list1       1 2 3 4 5

增
    插入数据时，如果该键不存在，则自动创建
    右边添加
        语法
            rpush key value。。。
        实例
            rpush list1 1 2 3 4 5
    左边添加
        语法
            lpush key value。。。
        实例
            lpush list1 7 8 9
查
    指定索引下标查询
        语法
            lrange key start stop
            lrange list1 0 3
            全部
            lrange list1 0 -1

        根据index查看
        lindex list1 1

改
    修改某个下标的值
    语法
        lset key index value
    实例
        lset list1 1 99

删
右边删除（尾部删除）
    语法
        rpop key
    实例
        rpop list1
左边删除（头部删除）
    语法
        lpop key
    实例
        lpop list1
删除指定的数据
    语法
    lrem key count value
    实例
    lrem list1 1 3
    若有多个3，删除所有的3
    则写 lrem lsit1 0 3
删除所有数据
    语法
        del key
    实例
        del list1

3.hash类型


"""
print('hello')