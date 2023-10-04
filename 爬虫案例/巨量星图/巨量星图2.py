# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 19:18
# @Author  : 4v1d
# @File    : 巨量星图2.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import requests
import hashlib
server_name = 'search.AdStarSearch'
service_method = 'SearchSpuVideoCase'
sort_type = '1'
limit = '30'
url = f'https://www.xingtu.cn/star_tools/api/gateway/handler_get/?keyword=&order_by=score&sort_type=1&page=1&limit=30&filters=%7B%22first_category_id%22:%22100%22,%22second_category_id%22:%2210000%22%7D&service_name={server_name}&service_method={service_method}&sign_strict=1&sign='
string = f"filtersfilterskeywordlimit{limit}order_byscorepage1service_method{service_method}service_name{server_name}sign_strict1sort_type{sort_type}e39539b8836fb99e1538974d3ac1fe98"
m = hashlib.md5()
m.update(string.encode())
sign = m.hexdigest()
print(requests.get(url=url+sign).text)