# -*- coding: utf-8 -*-
# @Time    : 2022/9/14 14:53
# @Author  : 4v1d
# @File    : 验证码1.py
# @Software: PyCharm
import requests
import ddddocr

def img_read():
    session = requests.session()
    ocr = ddddocr.DdddOcr()
    headers= {
    "Cookie": "SECKEY_ABVK=h8yFZK3rR3Dhjlw04+zo85VAFE4aWiEh1D8VCGMRw1k%3D; pageUrl=https%3A%2F%2Fapp.gjzwfw.gov.cn%2Fjmopen%2Fjmopen%2Fhomepage.do; JSESSIONID=354DFAE249306B47B6D34C846C2E513C; HWWAFSESID=8572f349c40d7810585; HWWAFSESTIME=1663138212739; JMOPENSESSIONID=00dfd0ab-a252-4f87-8a2c-484b6d13aaf4",
}
    session.headers = headers
    res = session.get('http://app.gjzwfw.gov.cn/jmopen/verifyCode.do?width=100&height=55&random=0.08462383677727381').content
    with open('ss.png','wb') as ffff:
        ffff.write(res)
    red = ocr.classification(res)
    return red

def ocr_img():
    session = requests.session()
    # 头部参数 顺序  反爬虫
    headers = {
    "Cookie": "SECKEY_ABVK=h8yFZK3rR3Dhjlw04+zo85VAFE4aWiEh1D8VCGMRw1k%3D; pageUrl=https%3A%2F%2Fapp.gjzwfw.gov.cn%2Fjmopen%2Fjmopen%2Fhomepage.do; JSESSIONID=354DFAE249306B47B6D34C846C2E513C; HWWAFSESID=8572f349c40d7810585; HWWAFSESTIME=1663138212739; JMOPENSESSIONID=00dfd0ab-a252-4f87-8a2c-484b6d13aaf4",
    "Referer": "http://app.gjzwfw.gov.cn/jmopen/webapp/html5/hnsqymckkfcx/index.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
    url = 'http://app.gjzwfw.gov.cn/jmopen/checkValiCode.do'
    s = img_read()
    session.headers = headers
    print(s.lower())
    data = {
        "code": s.lower()
    }
    res = session.post(url,data=data)
    print(res.text)

ocr_img()