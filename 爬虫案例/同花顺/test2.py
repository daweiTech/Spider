# -*- coding: utf-8 -*-
import copy
import random
import time

import requests
import pandas as pd
from tqdm import tqdm
from parsel import Selector



import execjs


# print(v)

def create_Cookie():
    with open('同花顺.js', encoding='utf-8') as f:
        x = f.read()
    # print(x)
    v = execjs.compile(x).call('get_Cookie')
    return v

data_Dic = {}
df_list = []
for page in tqdm(range(1, 21)):
    headers = {
        'hexin-v': create_Cookie(),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.77 Safari/537.36 '
    }
    url = f'http://q.10jqka.com.cn/usa/detailDefer/board/all/field/zdf/order/desc/page/{page}/ajax/1/'
    response = requests.request('Get', url, headers=headers)
    response.encoding = response.apparent_encoding
    trs = Selector(response.text).xpath('//table[@class="m-table m-pager-table"]/tbody//tr')

    for tr in trs:
        print('序号:',tr.xpath('./td[1]/text()').get())
        print('代码:',tr.xpath('./td[2]/a/text()').get())
        print('名称:',tr.xpath('./td[3]/a/text()').get())
        print('现价:',tr.xpath('./td[4]/text()').get())
        print('涨跌幅(%):',tr.xpath('./td[5]/text()').get())
        print('涨跌:',tr.xpath('./td[6]/text()').get())
        print('换手(%):',tr.xpath('./td[7]/text()').get())
        print('成交量:',tr.xpath('./td[8]/text()').get())
        print('市盈率(%):',tr.xpath('./td[9]/text()').get())
        print('成交额:',tr.xpath('./td[10]/text()').get())
        print('52周最高:',tr.xpath('./td[11]/text()').get())
        print('52周最低:',tr.xpath('./td[12]/text()').get())
        data_dic = copy.deepcopy(data_Dic)
        data_dic.update({'序号': tr.xpath('./td[1]/text()').get()})
        data_dic.update({'代码': tr.xpath('./td[2]/a/text()').get()})
        data_dic.update({'名称': tr.xpath('./td[3]/a/text()').get()})
        data_dic.update({'现价': tr.xpath('./td[4]/text()').get()})
        data_dic.update({'涨跌幅(%)': tr.xpath('./td[5]/text()').get()})
        data_dic.update({'涨跌': tr.xpath('./td[6]/text()').get()})
        data_dic.update({'换手(%)': tr.xpath('./td[7]/text()').get()})
        data_dic.update({'成交量': tr.xpath('./td[8]/text()').get()})
        data_dic.update({'市盈率(%)': tr.xpath('./td[9]/text()').get()})
        data_dic.update({'成交额': tr.xpath('./td[10]/text()').get()})
        data_dic.update({'52周最高': tr.xpath('./td[11]/text()').get()})
        data_dic.update({'52周最低': tr.xpath('./td[12]/text()').get()})
        df_list.append(data_dic)

    time.sleep(random.randint(5,10))

pd.DataFrame(df_list).to_excel('./同花顺.xlsx', index=False)

