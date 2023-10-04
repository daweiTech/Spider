# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 10:41
# @Author  : 4v1d
# @File    : Mongodb操作-01.py
# @Software: PyCharm
from pymongo import MongoClient
client = MongoClient()  # 建立连接
collection = client['Spiders']['海关1']
a = collection.distinct('相关编号')
print(len(a))

doc = collection.aggregate([{'$group':
                             {'_id':
                              {'相关编号':'$相关编号','中文名称':'$中文名称','决定税号':'$决定税号','规格型号':'$规格型号'},
                              'count' : {'$sum': 1}}},
                            {'$match': {'count': {'$gt': 1}}}],allowDiskUse = True)   #分组查询找到条目数大于1的记录
for i in doc:   #遍历每一个大于1的记录，删除第一条以后的记录
    first = 1   #定义0/1变量 判断是否为第一条  1：是  0：不是
    for j in collection.find(i["_id"]):
        if first == 1:
            first = 0  #等于0后说明不是第一条，第一条后的记录要删除
            continue
        else:   #firt != 1  删除重复记录除第一条后面的数据
            collection.delete_one({"_id":j["_id"]})