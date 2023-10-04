#导入需要的库
import json
from json.tool import main
import requests
import pymongo
import re
import json
#做好mongodb数据库连接
client = pymongo.MongoClient('127.0.0.1', port=27017)
db = client.Spiders
collection = db.icswb

class Spider:
    
    def __init__(self,url):
        self.url = url

    def get_data(self):
        headers = {
    "Host": "www.icswb.com",
    "Connection": "keep-alive",
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36",
    "Referer": "https://www.icswb.com/default.php?mod=channel&a=list&channel_id=105613&temp=default-column&slider_id=0&device_id=nklFzwW%2BHZRKn0lnZxgbMA%3D%3D&device_id_md5=82a1e492cbe6c881339364b91d10d698&device_type=1&AppVersion=6.0.0.6&AppVersionNum=6006&package_name=com.icswb.ChangshaInHand&api_version=6004",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en-US;q=0.8",
    "Cookie": "acw_tc=0b32973a16600309659224718e010839b51f7c8337f319aa1f3aa5e6711567"
}
        params = {
    "mod": "document_news",
    "a": "async_get_list",
    "jsonpcallback": "jQuery360009620074857499161_1660022151986",
    "channel_id": "105613",
    "p": "1",
    "ps": "10",
    "_": "1660022151987"
}
        r = requests.get(url=self.url,headers=headers,params=params)
        self.text = r.text

    def handle_data(self):
        data_list = re.findall('jQuery360009620074857499161_1660022151986\((.*)\)',self.text)
        # print(data_list[0])
        json_data = json.loads(data_list[0])
        data = json_data.get('result_list')

        for i in data:
            dict = {}
            dict['标题'] = i['DocumentNewsTitle']
            dict['发布时间'] = i['PublishDate']
            dict['主编'] = i['ManageUserName']
            content = i['DocumentNewsContent']
            data = re.findall('div style=\"text-align:justify; text-justify:inter-ideograph;\"><p>　　(.*)</p></div>',content)[0]
            data1 = data.replace('</p>','')
            dict['内容'] = data1.replace('<p>','')
            dict['关键人物'] = i["Author"]
            dict['来源'] = i["SourceName"]
            dict['类别'] = i['ChannelName']
            collection.insert(dict)


if __name__ == '__main__':
    url = 'https://www.icswb.com/default.php?mod=document_news&a=async_get_list&jsonpcallback=jQuery360009620074857499161_1660022151986&channel_id=105613&p=1&ps=10&_=1660022151987'
    s = Spider(url=url)
    s.get_data()
    s.handle_data()








