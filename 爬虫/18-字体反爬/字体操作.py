# -*- coding: utf-8 -*-
# @Time    : 2022/9/9 19:02
# @Author  : 4v1d
# @File    : 字体操作.py
# @Software: PyCharm
from fontTools.ttLib import TTFont
# 加载字体文件：
font = TTFont('file.woff')

# 转为xml文件：
font.saveXML('file.xml')

#font['glyf'][字体编码].coordinates
code_name_map = font.getBestCmap()


# for k,v in code_name_map.items():
#     if v[3:]:
#         a = '\\u00' + v[3:] if len(v[3:])==2 else '\\u' + v[3:]
#         b = a.encode("utf-8").decode("unicode_escape")
#         print(b)
for k,v in code_name_map.items():
    # print(k, v)
    try:
        a = '\\u00' + v[3:] if len(v[3:]) == 2 else '\\u' + v[3:]
        b = a.encode("utf-8").decode("unicode_escape")
        print(b)
    except:
        pass


