# -*- coding: utf-8 -*-
# @Time    : 2022/8/8 10:23
# @Author  : 4v1d
# @File    : selenium-08.py
# @Software: PyCharm

import requests,re

def get_data(num_id):
    data_url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/product/module/list/v2'
    headers = {
        'referer': 'https://category.vip.com/suggest.php?keyword=%E5%8F%A3%E7%BA%A2&ff=235%7C12%7C1%7C1&page=3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    params = {
        'callback': 'getMerchandiseDroplets2',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_NH',
        'fdc_area_id': '104104101',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '104104',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'user_id': '',
        'mars_cid': '1602569282048_0b4beb3d18306a0a0143c359ddb34fae',
        'wap_consumer': 'a',
        'productIds': '{}'.format(num_id),
        'scene': 'search',
        'standby_id': 'nature',
        'extParams': '{"stdSizeVids":"","preheatTipsVer":"3","couponVer":"v2","exclusivePrice":"1","iconSpec":"2x"}',
        'context': '',
        '_': '1603721644366',
    }
    response_2 = requests.get(url=data_url, params=params, headers=headers)
    print(response_2.text)
    titles = re.findall('"title":"(.*?)"', response_2.text, re.S)  # 标题
    salePrice = re.findall(',"salePrice":"(.*?)",', response_2.text, re.S)  # 售价
    marketPrice = re.findall('"marketPrice":"(.*?)"', response_2.text, re.S)  # 原价
    saleDiscount = re.findall('"saleDiscount":"(.*?)"', response_2.text, re.S)  # 折扣
    smallImage = re.findall('"smallImage":"(.*?)"', response_2.text, re.S)  # 商品图片地址
    lis = zip(titles, salePrice, marketPrice, saleDiscount, smallImage)
    dit = {}
    for li in lis:
        dit['商品名字'] = li[0]
        dit['售价'] = li[1]
        dit['原价'] = li[2]
        dit['折扣'] = li[3]
        dit['商品图片地址'] = li[4]
        print(dit)

for page in range(0, 1201, 120):
    url = 'https://mapi.vip.com/vips-mobile/rest/shopping/pc/search/product/rank'
    headers = {
        'referer': 'https://category.vip.com/suggest.php?keyword=%E5%8F%A3%E7%BA%A2&ff=235%7C12%7C1%7C1&page=3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    params = {
        'callback': 'getMerchandiseIds',
        'app_name': 'shop_pc',
        'app_version': '4.0',
        'warehouse': 'VIP_NH',
        'fdc_area_id': '104104101',
        'client': 'pc',
        'mobile_platform': '1',
        'province_id': '104104',
        'api_key': '70f71280d5d547b2a7bb370a529aeea1',
        'user_id': '',
        'mars_cid': '1602569282048_0b4beb3d18306a0a0143c359ddb34fae',
        'wap_consumer': 'a',
        'standby_id': 'nature',
        'keyword': '手环',
        'lv3CatIds': '',
        'lv2CatIds': '',
        'lv1CatIds': '',
        'brandStoreSns': '',
        'props': '',
        'priceMin': '',
        'priceMax': '',
        'vipService': '',
        'sort': '0',
        'pageOffset': '{}'.format(page),
        'channelId': '1',
        'gPlatform': 'PC',
        'batchSize': '120',
        '_': '1603721644362',
    }
    response = requests.get(url=url, params=params, headers=headers)
    ids = re.findall('"pid":"(.*?)"', response.text, re.S)
    for j in ids:
        get_data(j)





