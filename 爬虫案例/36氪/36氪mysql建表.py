# -*- coding: utf-8 -*-
# @Time    : 2022/9/2 9:07
# @Author  : 4v1d
# @File    : 36氪mysql建表.py
# @Software: PyCharm

import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',  # 输入数据库密码
    database='student',  # 数据库名
    charset='utf8'
)

conn = POOL.connection()
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql_createdb = """
CREATE TABLE IF NOT EXISTS `36Kr`(
                 id INT NOT NULL AUTO_INCREMENT,
                 `标题`  CHAR(100),
                 `作者` CHAR(10),
                 `摘要` CHAR(100),
                 `详情链接` CHAR(100),
                 `时间` CHAR(10),
                 PRIMARY KEY(id)
                 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
# cursor.execute(sql_createdb)

dict = {'标题': '时代的眼泪？“有妖气”将关停，代表作有《十万个冷笑话》《镇魂街》', '作者': '36氪的朋友们', '摘要': '在“有妖气”原地踏步时，中国漫画平台却在移动互联网中迎来快速扩张的黄金期', '详情链接': 'https://36kr.com/p/1897718313920904', '时间': '54秒前'}
sql_insert = "insert into 36Kr( `标题`, `作者`, `摘要`, `详情链接`,`时间`) values (\"%s\",\"%s\",\"%s\"," \
      "\"%s\",\"%s\")" % (str(dict['标题']), str(dict['作者']),str(dict['摘要']),str(dict['详情链接']),str(dict['时间']))

cursor.execute(sql_insert)
conn.commit()
cursor.close()
conn.close()
