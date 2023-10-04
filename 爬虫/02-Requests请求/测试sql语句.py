# -*- coding: utf-8 -*-
# @Time    : 2022/7/29 19:53
# @Author  : 4v1d
# @File    : 测试sql语句.py
# @Software: PyCharm

sql = 'CREATE TABLE IF NOT EXISTS infomation ' \
      '(id VARCHAR(255) NOT NULL, ' \
      'address VARCHAR(255) NOT NULL, ' \
      'city_name VARCHAR(255) NOT NULL, ' \
      'decoration VARCHAR(255) NOT NULL,' \
      'district VARCHAR(255) NOT NULL,' \
      'titile  VARCHAR(255) NOT NULL,' \
      'show_price_info VARCHAR(255) NOT NULL,' \
      'PRIMARY KEY (id))'


def generate_sql(data_list):
      data = data_list[0]
      cols = ", ".join('`{}`'.format(k) for k in data.keys())
      val_cols = ', '.join('%({})s'.format(k) for k in data.keys())
      sql = """
    INSERT INTO information(%s) VALUES(%s)
    """ % (cols, val_cols)
      return sql

list_test = [{'address': '长沙市开福区黄兴北路112号', 'city_name': '长沙市', 'decoration': '毛坯', 'district': '开福', 'title': '华润置地中心', 'show_price_info': '均价9000元/平'}, {'address': '湖南省长沙市望城区', 'city_name': '长沙市', 'decoration': '非毛坯', 'district': '岳麓', 'title': '阳光城溪山悦', 'show_price_info': '均价8300元/平'}, {'address': '岳麓雅礼洋湖中学南门', 'city_name': '长沙市', 'decoration': '非毛坯', 'district': '岳麓', 'title': '华润凯旋门', 'show_price_info': '均价15800元/平'}, {'address': '雨花区万家丽南路二段599号', 'city_name': '长沙市', 'decoration': '毛坯', 'district': '雨花', 'title': '中南国际眼镜城', 'show_price_info': '总价78万/套'}, {'address': '人民路中交牛津街', 'city_name': '长沙市', 'decoration': '毛坯', 'district': '芙蓉', 'title': '中交牛津街', 'show_price_info': '均价17000元/平'}, {'address': '香樟路与曙光路交汇处西北角', 'city_name': '长沙市', 'decoration': '毛坯', 'district': '雨花', 'title': '华润翡翠府', 'show_price_info': '均价7000元/平'}, {'address': '雷锋大道与星月路交汇处东南角(长沙医学院对面)', 'city_name': '长沙市', 'decoration': '毛坯', 'district': '望城', 'title': '美的翰城', 'show_price_info': '均价6200元/平'}, {'address': '东二环二段690号', 'city_name': '长沙市', 'decoration': '毛坯', 'district': '开福', 'title': '海洋半岛', 'show_price_info': '均价9800元/平'}, {'address': '东风路248号（鸥波港湾旁）', 'city_name': '长沙市', 'decoration': '毛坯', 'district': '开福', 'title': '上园', 'show_price_info': '均价12000元/平'}, {'address': '金星北路与月亮岛路交汇处', 'city_name': '长沙市', 'decoration': '毛坯', 'district': '望城', 'title': '明发国际城', 'show_price_info': '价格待定'}]
print(generate_sql(list_test))
print(sql)
# import time,random
# for x in range(1, 10):
#       j = x / 10
#       print(j)
#       a = (random.randint(400, 800) / 1000)
#       print(a)
for x in range(1, 10):
    j = x / 10
    k = 0.00
    for y in range(1, 11):
        js = f"document.documentElement.scrollTop = document.documentElement.scrollHeight * {round((j+k),2)}"
        print(js)
        k+=0.01