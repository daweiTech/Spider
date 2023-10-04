# -*- coding: utf-8 -*-
# @Time    : 2022/8/4 17:39
# @Author  : 4v1d
# @File    : 爬取王者荣耀.py
# @Software: PyCharm

import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=4&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1659604934191'
r = requests.get(url=url)
res = r.json().get('List')
print(res)
r1 = r.json()
print(r1)