from selenium import webdriver
import pymysql
from dbutils.pooled_db import PooledDB
import time
from selenium.webdriver.common.action_chains import ActionChains
import re



driver_path = r'F:\Python-项目\weixing\Scripts\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# get 方法会一直等到页面被完全加载，才会继续程序
time.sleep(2)
driver.get('https://www.newrank.cn/public/info/list.html?period=week&type=data')

datalist = []
def function():
    for i in range(1, 21):
        data1 = []
        time.sleep(2)
        name = driver.find_element_by_xpath('//*[@id="table_list"]/tbody/tr[{}]/td[2]/div/h4/a'.format(int(i)))
        data1.append(name.text)  # 公众号名字
        read = driver.find_element_by_xpath('//*[@id="table_list"]/tbody/tr[{}]/td[4]'.format(int(i)))
        data1.append(read.text)  # 公众号总阅读数
        zan = driver.find_element_by_xpath('//*[@id="table_list"]/tbody/tr[{}]/td[8]'.format(int(i)))
        data1.append(zan.text)  # 公众号总点赞数
        see = driver.find_element_by_xpath('//*[@id="table_list"]/tbody/tr[{}]/td[9]'.format(int(i)))
        data1.append(see.text)  # 公众号总在看数
        number = driver.find_element_by_xpath('//*[@id="table_list"]/tbody/tr[{}]/td[10]/p'.format(int(i)))
        data1.append(number.text)  # 公众号总在看数
        if flag==0:
            data1.append('文化')
        elif flag==1:
            data1.append('百科')
        elif flag==2:
            data1.append('健康')
        elif flag==3:
            data1.append('时尚')
        elif flag==4:
            data1.append('美食')
        elif flag==5:
            data1.append('乐活')
        elif flag==6:
            data1.append('旅行')
        elif flag==7:
            data1.append('幽默')
        name = driver.find_element_by_xpath('//*[@id="table_list"]/tbody/tr[{}]/td[2]/i'.format(i))
        result = re.findall(r'[(]["](.*?)["][)]', name.get_attribute('style'))
        data1.append(result[0])
        datalist.append(data1)

    for i in range(1, 31):
        button = driver.find_element_by_xpath('//*[@id="rank_data"]/div/p/a')
        driver.execute_script("$(arguments[0]).click()", button)  # 加载剩余页面
        data1 = []

        name = driver.find_element_by_xpath('//*[@id="more_list"]/tbody/tr[{}]/td[2]/div/h4/a'.format(int(i)))
        data1.append(name.text)  # 公众号名字
        read = driver.find_element_by_xpath('//*[@id="more_list"]/tbody/tr[{}]/td[4]'.format(int(i)))
        data1.append(read.text)  # 公众号总阅读数
        zan = driver.find_element_by_xpath('//*[@id="more_list"]/tbody/tr[{}]/td[8]'.format(int(i)))
        data1.append(zan.text)  # 公众号总点赞数
        see = driver.find_element_by_xpath('//*[@id="more_list"]/tbody/tr[{}]/td[9]'.format(int(i)))
        data1.append(see.text)  # 公众号总在看数
        number = driver.find_element_by_xpath('//*[@id="more_list"]/tbody/tr[{}]/td[10]/p'.format(int(i)))
        data1.append(number.text)  # 公众号总在看数
        if flag==0:
            data1.append('文化')
        elif flag==1:
            data1.append('百科')
        elif flag==2:
            data1.append('健康')
        elif flag==3:
            data1.append('时尚')
        elif flag==4:
            data1.append('美食')
        elif flag==5:
            data1.append('乐活')
        elif flag==6:
            data1.append('旅行')
        elif flag==7:
            data1.append('幽默')
        name = driver.find_element_by_xpath('//*[@id="more_list"]/tbody/tr[{}]/td[2]/i'.format(i))
        result = re.findall(r'[(]["](.*?)["][)]', name.get_attribute('style'))
        data1.append(result[0])
        datalist.append(data1)
flag = 0
for i in range(1,9):#提取前8个分类，1-8
    href1 = driver.find_element_by_css_selector('#day_life_links > a:nth-child({})'.format(i))
    ActionChains(driver).click(href1).perform()
    function()
    flag+=1





POOL = PooledDB(
    creator=pymysql,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',  # 输入数据库密码
    database='wechat',  # 数据库名
    charset='utf8'
)
def saveWeChatArticle(dict):
    conn = POOL.connection()
    cursor = conn.cursor()
    sql = "insert  into Official_Accounts (`tname`, `tread`,`zan`,`see`,`number`,`ttype`,`url`) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
    str(dict[0]), str(dict[1]),str(dict[2]),str(dict[3]),str(dict[4]),str(dict[5]),str(dict[6]))
    # sql 是字符串；因此变量s%处，用转义字符 \" 输入双引号，后面，用str 将每个值转为str类型；
    cursor.execute(sql)
    conn.commit()  # 提交到数据库
    cursor.close()
    conn.close


for item in datalist:
    saveWeChatArticle(item)#保存数据到数据库

