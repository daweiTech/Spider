import requests
from lxml import etree
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import pymongo


client = pymongo.MongoClient('127.0.0.1', port=27017)
db = client.Spiders
collection = db.weipinghui

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(options=options)
browser.get('https://category.vip.com/suggest.php?keyword=%E5%8F%A3%E7%BA%A2&ff=235|12|1|1')
time.sleep(6)

def drop_down():
    for x in range(1, 10):
        j = x / 10
        js = f"document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}"
        browser.execute_script(js)
        time.sleep(random.randint(400,800)/1000)

drop_down()

def save_mongo(data):
    if isinstance(data, dict):
        collection.insert(data)

html = browser.page_source
html_source = etree.HTML(html)
datas = html_source.xpath("//section[@class='goods-list c-goods-list--normal']/div")
i = 0
for data in datas[1:]:
    item = {}
    detail_url= data.xpath('./a/@href')[0]
    item['详情链接'] = detail_url.replace('//','')
    img_url = data.xpath('./a/div/div/img/@src')[0]
    item['图片链接'] = img_url.replace('//','')
    item['商品名称'] = data.xpath('./a/div/div/img/@alt')[0]
    tag = data.xpath('./a/div/ul/li/span/text()')
    item['标签'] = ''.join(tag)
    sale_price = data.xpath('./a/div/div/div/div[@class="c-goods-item__sale-price J-goods-item__sale-price"]/text()')[0]
    item['价格'] = sale_price
    save_mongo(item)
    i+=1

print("当前页面总共{}条数据".format(len(datas)-1))
print("收集到的数据{}条".format(i))



