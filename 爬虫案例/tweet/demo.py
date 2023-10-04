import json
with open('data.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
datas = json_data['data']['threaded_conversation_with_injections_v2']["instructions"][0]['entries']
print(len(datas))
for i in datas[0:9]:
    print(len(i["content"]["items"]))
    if len(i["content"]["items"])==2:
        mid = i["content"]["items"][0]["item"]["itemContent"]["tweet_results"]["result"]["legacy"]
        mid1 = i["content"]["items"][1]["item"]["itemContent"]["tweet_results"]["result"]["legacy"]
        item = {
        '发布时间': mid['created_at'],
        '推特名字':mid['entities']['user_mentions'][0]['name'],
        '作者全名':mid['entities']['user_mentions'][0]['screen_name'],
        '作者id':mid['entities']['user_mentions'][0]['id_str'],
        '点赞数':mid['favorite_count'],
        '发布内容':mid['full_text']
    }
        item1 = {
        '发布时间': mid1['created_at'],
        '推特名字':mid1['entities']['user_mentions'][0]['name'],
        '作者全名':mid1['entities']['user_mentions'][0]['screen_name'],
        '作者id':mid1['entities']['user_mentions'][0]['id_str'],
        '点赞数':mid1['favorite_count'],
        '发布内容':mid1['full_text']
    }
        print(item)
        print(item1)
    else:
        mid = i["content"]["items"][0]["item"]["itemContent"]["tweet_results"]["result"]["legacy"]
        item = {
        '发布时间': mid['created_at'],
        '推特名字':mid['entities']['user_mentions'][0]['name'],
        '作者全名':mid['entities']['user_mentions'][0]['screen_name'],
        '作者id':mid['entities']['user_mentions'][0]['id_str'],
        '点赞数':mid['favorite_count'],
        '发布内容':mid['full_text']
    }
        print(item)


    # print(item1)
    # print(i["content"]["items"][1]["item"]["itemContent"]["tweet_results"]["result"]["legacy"])
    
# for i in datas:
#     for j in i['content']['items']:
#         for k in(j['item']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']):
#             print(k[''])
#     break
