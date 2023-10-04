# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 15:29
# @Author  : 4v1d
# @File    : 01-script1.py
# @Software: PyCharm


"""
不是关系数据库，是面向文档的数据库
隐式创建
show dbs

dbs.dropDatabase()

db.createCollection('stu')

show collections

db.stu.insert({'name':'sam'})#自动配id

    自己插入id
    db.stu.insert({'_id':1,name':'sam',age:18})


查询

一般查询
        db.集合名称.find()
        db.stu.find()

美式查询,格式更好看点
        db.集合名称.find()。pretty()
        db.stu.find().pretty()

    插入多条语法
        db.集合名称.insert([
            一条文档,
            二条文档,
            三条文档
        ])

    实例
        db.集合名称.insert([
           {'_id':1,name':'sam',age:18},
            {'_id':1,name':'sam',age:18},
            {'_id':1,name':'sam',age:18}
        ])

    指定查询
    db.stud.find({name:'sam'})


    查询性别女，年龄为16
    db.stu.find({$and:[{sex:'女'},{age:16}]})
    and的中括号里面用逗号分隔条件，每个条件都是字典格式

    查询
    1.女16
    2.男大于等于18
    db.stu.find({$or:
    {$and:[{sex:'女'},{age:16}]},
    {$and:[{sex:'男'},{age:{$gte:18}}]}
    ]
    })

    改
        1.只会修改一条数据 并且其他字段也没有了
        dbu.stu.update({name:'sam'},{name:'jack'})
        sam修改为jack，之前添加的其他好几条数据没了

        2.只会修改一条数据 并且其他字段保留
        dbu.stu.update({name:'sam'},{$set:{age:66}})
        sam的年龄进行修改，其他不动

        3.修改多条
        dbu.stu.update({name:'sam'},{$set:{age:66}},{multi:true})


"""
