# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 21:02
# @Author  : 4v1d
# @File    : Redis-去重.py
# @Software: PyCharm
import redis
import hashlib

class Redis():
    def __init__(self):
        self.con = redis.Redis(
            host='192.168.40.128', #ip地址
            port=6379, #端口号，默认为6379
            db=0,
            decode_responses=True #设置为True存的数据格式就是str类型
        )
    def add(self,key,data):
        if self.exit(key,data):
            print("该数据已存在！")
        else:
            self.con.sadd(key,data) #添加
            print("添加成功")
    def query(self,key):
        return self.con.smembers(key)  #拿出key对应所有值
    def delete(self,key):
        self.con.delete(key) #删除key键
    def exit(self,key,data):
        return self.con.sismember(key, data)  # 判断key里是否有data，有则返回true

class Hashencode():
    def __init__(self):
        self.encode_machine = hashlib.md5()  # 创建一个md5对象
    def encode(self,url):
        self.encode_machine.update(url.encode()) #更新
        url_encode = self.encode_machine.hexdigest() #拿到编码后的十六进制数据
        return url_encode


