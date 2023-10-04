from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import random

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
with open('stealth.min.js') as f:
    js = f.read()

print("开启webdriver,爬取数据开始")
driver_path = r'F:\Python-项目\weixing\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path,chrome_options = options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": js
})

time.sleep(2)
# driver.get('https://www.newrank.cn/public/info/list.html?period=month&type=data')

import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',  # 输入数据库密码
    database='test',  # 数据库名
    charset='utf8'
)

conn = POOL.connection()
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# sql = """ SELECT tname FROM overall_list
#            LIMIT 478,1000
#     """
sql = """
SELECT tname FROM overall_list WHERE tname NOT in (SELECT tname FROM signal_officialcount)
"""
# sql = """SELECT  tname,tread,zan,see FROM official_accounts
#          limit 100
# """
cursor.execute(sql)
result = cursor.fetchall()

cursor.close()
conn.close()

def saveWeChatArticle(dict):
    conn = POOL.connection()
    cursor = conn.cursor()
    sql = "insert  into signal_officialcount (`tname`,`ttype`,`ttag`,`tfan`,`taccount`,`tinfo`,`introduction`) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (str(dict[0]), str(dict[1]),str(dict[2]),str(dict[3]),str(dict[4]),str(dict[5]),str(dict[6]))
    # sql 是字符串；因此变量s%处，用转义字符 \" 输入双引号，后面，用str 将每个值转为str类型；
    cursor.execute(sql)
    conn.commit()  # 提交到数据库
    cursor.close()
    conn.close
datalist = []
def bianli():
    for i in range(1, 21):
        # data = []
        name = driver.find_element_by_xpath('//*[@id="table_list"]/tbody/tr[{}]/td[2]/div/p/a'.format(int(i)))
        datalist.append(name.text)  # 公众号名字

    button = driver.find_element_by_xpath('//*[@id="rank_data"]/div/p/a')
    driver.execute_script("$(arguments[0]).click()", button)  # 加载剩余页面

    for i in range(1, 481):
        name = driver.find_element_by_xpath('//*[@id="more_list"]/tbody/tr[{}]/td[2]/div/p/a'.format(int(i)))
        datalist.append(name.text)


time.sleep(2)

driver.get('https://www.newrank.cn/public/info/list.html?period=month&type=data')
bianli()
# for i in range(1,2):
#     href1 = driver.find_element_by_css_selector('#day_life_links > a:nth-child({})'.format(i))
#     ActionChains(driver).click(href1).perform()
#     bianli()
# time.sleep(2)

print(datalist)
print(len(datalist))

# time.sleep(2)

def shouji():
    data = []
    name = driver.find_element_by_css_selector(
        '#root > div.new-detailContainer--2RUPS > div.new-headContainer--W5ImF > div.new-accountInfo--73bUW > div.new-accountIntroduce--2I4cc > div.new-accountBasicInfo--3iwum > div.new-accountName--1B_Hs > div')

    data.append(name.text)  # 名字

    type = driver.find_element_by_css_selector(
        '#root > div.new-detailContainer--2RUPS > div.new-headContainer--W5ImF > div.new-accountInfo--73bUW > div.new-accountNewrank--21n0s > div:nth-child(1) > div > span > span')

    data.append(type.text)  # 种类

    tag = driver.find_element_by_css_selector(
        '#root > div.new-detailContainer--2RUPS > div.new-headContainer--W5ImF > div.new-accountInfo--73bUW > div.new-accountNewrank--21n0s > div:nth-child(2) > div > div > span > span')

    data.append(tag.text)  # 标签

    fan = driver.find_element_by_css_selector(
        '#root > div.new-detailContainer--2RUPS > div.new-headContainer--W5ImF > div.new-accountInfo--73bUW > div.new-accountNewrank--21n0s > div:nth-child(3) > div')

    data.append(fan.text)  # 预估粉丝数

    account = driver.find_element_by_css_selector(
        '#root > div.new-detailContainer--2RUPS > div.new-headContainer--W5ImF > div.new-accountInfo--73bUW > div.new-accountIntroduce--2I4cc > div.new-accountBasicInfo--3iwum > div:nth-child(2)')
    data.append(account.text)  # 微信号

    info = driver.find_element_by_css_selector(
        '#root > div.new-detailContainer--2RUPS > div.new-headContainer--W5ImF > div.new-accountInfo--73bUW > div.new-accountIntroduce--2I4cc > div.new-accountBasicInfo--3iwum > div:nth-child(3)')
    data.append(info.text)  # 公司

    introduction = driver.find_element_by_css_selector(
        '#root > div.new-detailContainer--2RUPS > div.new-headContainer--W5ImF > div.new-accountInfo--73bUW > div.new-accountIntroduce--2I4cc > div.new-accountBasicInfo--3iwum > div.new-synopsis--1TlMb > span.new-description--TXa1S')

    data.append(introduction.text)  # 介绍
    print(data)
    return data


for j in range(300,500):
    driver.implicitly_wait(10)
    driver.get('https://newrank.cn/new/?account={}'.format(datalist[j]))
    if (j==0):
        time.sleep(60)
    elif j%3==0:
        time.sleep(5)
    else:
        time.sleep(random.randint(3, 5))
    try:
        driver.implicitly_wait(10)
        result = shouji()
        # print(result)
        saveWeChatArticle(result)
        time.sleep(2)
    except Exception as e:
        driver.refresh()
        driver.implicitly_wait(10)
        try:
            driver.implicitly_wait(10)
            result = shouji()
            saveWeChatArticle(result)
            time.sleep(2)
        except Exception as e:
            pass
driver.close()



