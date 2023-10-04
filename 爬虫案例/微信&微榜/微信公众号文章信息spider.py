import pymysql
from dbutils.pooled_db import PooledDB
import time
# 毫秒转化为日期
def getDate(times):
    timearr = time.localtime(times)
    date = time.strftime("%Y-%m-%d %H:%M:%S", timearr)
    return date
POOL = PooledDB(
    creator=pymysql,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',  # 输入数据库密码
    database='test',  # 数据库名
    charset='utf8'
)
POOL1 = PooledDB(
    creator=pymysql,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',  # 输入数据库密码
    database='wechat',  # 数据库名
    charset='utf8'
)

POOL2 = PooledDB(
    creator=pymysql,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',  # 输入数据库密码
    database='test',  # 数据库名
    charset='utf8'
)

conn = POOL2.connection()
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# sql = """ SELECT tname FROM overall_list
#            LIMIT 478,1000
#     """
# sql = """
# SELECT DISTINCT tname FROM overall_list WHERE tname NOT in(SELECT nickname FROM wechat_article)
# """
sql = """
select nickname from wechat_article GROUP BY nickname HAVING(COUNT(nickname)<10) 
"""
# sql = """SELECT  tname,tread,zan,see FROM official_accounts
#          limit 100
# """
cursor.execute(sql)
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()


def saveWeChatArticle(dict):
    conn = POOL.connection()
    cursor = conn.cursor()
    sql = "insert  into wechat_article ( `title`, `update_time`, `link`, `cover`,`nickname`) values(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
    str(dict[0]), str(dict[1]),str(dict[2]),str(dict[3]),str(dict[4]))
    # sql 是字符串；因此变量s%处，用转义字符 \" 输入双引号，后面，用str 将每个值转为str类型；
    cursor.execute(sql)
    conn.commit()  # 提交到数据库
    cursor.close()
    conn.close
import requests
import json
import random

print("收集开始")
Cookie = 'ua_id=CxOVyOgcHAxmFXu3AAAAAG35jgP4K-hOFR9A-sqosCc=; wxuin=48288643364322; mm_lang=zh_CN; rand_info=CAESIFtpgP84DNwpZ5QAeuknmnWuO4SL5llrFmpx+QyD+rXY; slave_bizuin=3937343144; data_bizuin=3937343144; bizuin=3937343144; data_ticket=PqT0N8RcWVA83a1AKNhqGnjnp0SXrk2IewL9yI9FTLI0DIDhlVt3DQ8KfTgwYetj; slave_sid=OEdkMDJBUkRRMWJqODZIQkZaRnU3bFk0TkFJd29jNjBiaUQ5cEJFMG5oM1lqQTJpV0Z2azBMSVllSktvd3lfclNCaW1NTjFnN1JaTzNyTEhCVVpiMkZQcDc4QjB0eEVmSUFYdElQQTlNbl9MRWRycTRxMFFKdGNKVGJqNFYyZ0Z1MXNpZkplOWM3Umg1MjZp; slave_user=gh_ed2cf4c7f92e; xid=34003efed278079d3a95a33bce285376; pgv_pvid=6466279416'
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
headers = {
  "Cookie": Cookie,
  "User-Agent": 'Mozilla/5.0 (Linux; Android 10; YAL-AL00 Build/HUAWEIYAL-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.64 HuaweiBrowser/10.0.1.335 Mobile Safari/537.36'
    }


token = '1310364201'        # 获取方法：如上述 直接复制下来,1179580055

for i in result:
    keyword = i['nickname']  # 公众号名字：可自定义,i['nickname'] 有三处
    search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?action=search_biz&begin=0&count=5&query={}&token={}&lang=zh_CN&f=json&ajax=1'.format(keyword,token)
    print(search_url)
    sleepTime = random.randint(3, 10)
    print(sleepTime)
    time.sleep(sleepTime)
    doc = requests.get(search_url,headers=headers).text
    jstext = json.loads(doc)
    fakeid = jstext['list'][0]['fakeid']
    print(fakeid,i['nickname'])#i['nickname']
    data = {
        "token": token,
        "lang": "zh_CN",
        "f": "json",
        "ajax": "1",
        "action": "list_ex",
        "begin": 0,
        "count": "5",
        "query": "",
        "fakeid": fakeid,
        "type": "9",
        }
    for k in range(0,1):
        data["begin"] = k * 5#决定翻页
        content_json = requests.get(url, headers=headers, params=data).json()
        # print(content_json)
        datalist = []
        j = 0
        dict = content_json["app_msg_list"]
        # print(len(dict))
        for l in range(len(dict)):
            import re
            k = re.sub('"', '',dict[l]["title"])#一些文章题目可能有双引号，需要去掉否则后面sql语句会报错
            print(k)
            items = [k, getDate(dict[l]["update_time"]), dict[l]["link"], dict[l]["cover"], ''.join(i['nickname'])]#i['nickname'],i['tname']
            print(items)
            saveWeChatArticle(items)  # 调用 savewechatarticle() 存入数据库
            j+=1
            print(j)
        sleepTime = random.randint(3, 10)
        print(sleepTime)
        time.sleep(sleepTime)
        # for item in content_json["app_msg_list"]:
        #     if j == 2:
        #         break
        #     else:
        #         print(item)
        #         import re
        #         k = re.sub('"', '',item["title"])#一些文章题目可能有双引号，需要去掉否则后面sql语句会报错
        #         print(k)
        #         items = [k, getDate(item["update_time"]), item["link"], item["cover"], ''.join(i['tname'])]#i['nickname']
        #         print(items)
        #         saveWeChatArticle(items)  # 调用 savewechatarticle() 存入数据库
        #         sleepTime = random.randint(3, 10)
        #         print(sleepTime)
        #         time.sleep(sleepTime)
        #         j+=1
        #         continue


print("收集结束")








