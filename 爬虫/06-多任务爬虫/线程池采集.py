# -*- coding: utf-8 -*-
# @Time    : 2022/8/5 16:52
# @Author  : 4v1d
# @File    : 线程池采集.py
# @Software: PyCharm

from concurrent.futures.thread import ThreadPoolExecutor
import time
import requests

def download_one_page(data: dict):
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    headers = {
        'user-agent': '123123asdasdasd',
        'referer': 'http://www.xinfadi.com.cn/priceDetail.html'
    }

    resp = requests.post(url=url, headers=headers, data=data)
    print(resp.status_code)


def download_pages(page_start: int, page_end: int, page_limit: int = 20):

    with ThreadPoolExecutor(100) as t:
        for i in range(page_start, page_end + 1):
            data = {
                'limit': f'{page_limit}',
                'current': f'{i}',
                'pubDateStartTime': '',
                'pubDateEndTime': '',
                'prodPcatid': '',
                'prodCatid': '',
                'prodName': ''
            }
            t.submit(download_one_page,data)

if __name__ == '__main__':
    start_time = time.time()
    download_pages(page_start=1, page_end=100, page_limit=20)
    end_time = time.time()
    print(f'总耗时{end_time - start_time}s')