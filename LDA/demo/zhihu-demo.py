# -*- coding: utf-8 -*-
# @Time    : 2022/11/2 14:19
# @Author  : 4v1d
# @File    : zhihu-demo.py
# @Software: PyCharm

import pandas as pd
import os
import re
import jieba
# 下面的 url 是 csv 文件的远程链接，如果你缺失这个文件，则需要用浏览器打开这个链接
# 下载它，然后放到代码运行命令，且文件名应与下面的 csv_path 一致
url = 'https://raw.githubusercontents.com/Micro-sheep/Share/main/zhihu/answers.csv'
# 本地 csv 文档路径
csv_path = 'answers.csv'
# 待分词的 csv 文件中的列
document_column_name = '回答内容'
pattern = u'[\\s\\d,.<>/?:;\'\"[\\]{}()\\|~!\t"@#$%^&*\\-_=+a-zA-Z，。\n《》、？：；“”‘’｛｝【】（）…￥！—┄－]+'

if not os.path.exists(csv_path):
    print(f'请用浏览器打开 {url} 并下载该文件(如果没有自动下载，则可以在浏览器中按键盘快捷键 ctrl s 来启动下载)')
    os.exit()
df = (
    pd.read_csv(
        csv_path,
        encoding='utf-8-sig')
    .drop_duplicates()
    .rename(columns={
        document_column_name: 'text'
    }))

# 去重、去缺失、分词
df['cut'] = (
    df['text']
    .apply(lambda x: str(x))
    .apply(lambda x: re.sub(pattern, ' ', x))
    .apply(lambda x: " ".join(jieba.lcut(x)))
)
print(df['cut'])
