# -*- coding: utf-8 -*-
# @Time    : 2022/7/24 15:53
# @Author  : 4v1d
# @File    : demo2.py
# @Software: PyCharm

import httpx
#爬图片样例
class Demo():

    def __init__(self):
        pass

    def url_list(self):
        url_list = ["https://img.vm.laomishuo.com/image/2019/12/2019122210292813-scaled.jpeg",
                    "https://img.vm.laomishuo.com/image/2019/12/2019122210294290-scaled.jpeg",
                    "https://img.vm.laomishuo.com/image/2019/12/2019122210295639-scaled.jpeg"]
        return url_list

    def main(self):
        url = self.url_list()
        for index,u in enumerate(url):
            res = httpx.get(u)
            self.save(res.content,index)
            #print(res.text.encode())#res.content

    def save(self,byte,index):
        with open(str(index)+'.jpg','wb') as f:
            f.write(byte)

if __name__ == '__main__':
    Demo().main()