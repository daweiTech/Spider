# -*- coding:utf-8 -*-
import json
import math
import random
import time
from datetime import datetime
import logging
import requests
import sys
import sql
from chromedriver import user_agent_list

headers = {
    'Cookie': 'NMTID=00OkAOMPWyyR_XHxk58km79lBZ8J_gAAAGCQ8TrQg; _ntes_nuid=334eef1fb133c6b3736495df7eb4bd4c; _ntes_nnid=334eef1fb133c6b3736495df7eb4bd4c,1659946607010; _ga=GA1.1.1682044360.1660117884; _clck=1lsi84k|1|f3w|0; Qs_lvt_382223=1660117884,1660117981; Qs_pv_382223=708639631080738800,3504784567074095600; _ga_C6TGHFPQ1H=GS1.1.1660117884.1.1.1660118746.0; __root_domain_v=.163.com; _qddaz=QD.548262825960126; P_INFO=ldavid123@163.com|1663775064|0|youdao_jianwai|00&99|null&null&null#not_found&null#10#0|&0||ldavid123@163.com; WNMCID=xnthki.1666068618666.01.0; WEVNSM=1.0.0; WM_TID=EtnwEaAj3VhBFQAFAUKAVIblihRyrTfP; __bid_n=18413f037be54e14364207; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8db464adacf895d57bbab88ba2c84a868a9f86d4469c8f88b3b653878c8ab4f82af0fea7c3b92ab6be9ea7ef5bb797a6d5e64d94e9fd92d46f93edfc99cc648f9d8c8ef360edefba9acd3b8b98a7d2c63fa78aaa96b76d819cfe85d87bfbef8396ec7bfceafc8ec1468bb3c09bef6ea28c8ed2aa7c8fab8bd4f146b8ed82afed7ff59effb1d44997aabaaad63b8ab583d8b764ed86c0d9ce6892b0fb90bc219af1a7add64e8d929f8fdc37e2a3; WM_NI=vbRFlQuIj4gGP73qQeQ34xIhMCDmpT/1vyN1IHi1G5eVfu4gCD2dUq91Muiq864mBNImpzlfbTB1+pMuE3rNt3NNnu7B1PQCUvvIW1JkM74h/Zp8OlRp5o9+Z/iLWFONQnY=; _iuqxldmzr_=33; JSESSIONID-WYYY=hZ+jCzzdbX+AGgweaxuxdd8mdO/P53Bth0XpEaG7uy24VVbaCX6FWlw/AbdGlOzjJc3aEJCe5Mm/JCXPnuA9OPdZ+d436yljw7wjYBhnDrQ65d5XmkmJ12w+RijibBYuIRrsd3tQ7TpQtzUFXMMPUUDi6PWvsfr7ND6Hz4zxUMrRtkMK:1667543771742; __snaker__id=062FVhCbhlAXpy5a; gdxidpyhxdE=hNolkSkvqOZ2ZfgKqefehYdy1frPIjqmNgxSXnp22zTimD2Lij4QCOHEa0mxJBJqcNpj0dLhu9RmxSgnT5N24Xw4kHDkSpH0cKViYAtPzZI+wkZjbynCpkmkSC2/O8t3ppDp7CkXOR+a6meJfYzrJiqv6ezcVt334BIPZ8jdQLcubo4o:1667542872287; YD00000558929251:WM_NIKE=9ca17ae2e6ffcda170e2e6ee8bc825b2b3888af3669cbc8fa7c55f978b8b87d170889e98b9f533a39b9eabf82af0fea7c3b92ab0aeb7a6b874a1f5a9d3c566fcbbe5ade446f5f0e1dae26df8e7f896f13e90e7b9d8b5668797afa4c66b899fa8d6fc5caa8da2afe47393adbeb2d55292ebc0b3c95d92a7e1b0ee39f6a8b791b43d9c9ef78ec94191aabcd3c93bf294aeb9cc638af1abccae5ff6aef8d6ed46fcbeb996b780ac9d9894c16ff3e98584b86aaba89bd3b337e2a3; YD00000558929251:WM_NI=lryE5xc+g2Fn8e+LaN70/9cg498ur6L9w76nEIaCGaKAh5yPjSnNayQsrQVZR5pRJWRy/Oo36xyp17XB9mJKSvt2J12LbXIiJ/e+/U6r85nN8bwu4thCXsBe17Kc5bixU20=; YD00000558929251:WM_TID=fa7eeyp15uBBAVUEUBLBcHVXH69KVUZ7; MUSIC_U=cddda8f574adbb75568c568db07c4b525459d6640179ac98e5389ff3fe87ef46993166e004087dd32ee39068677a3338db21cd1ee210f7e1383c98c1882c1c24dcb695dcffa7813dd4dbf082a8813684; __csrf=af4271c7730725e97a776b79e7b555ae; __remember_me=true; ntes_kaola_ad=1',#更换为自己的cookie,登录网易云音乐pc版,F12里获取
    'Referer': 'http://music.163.com/',
    'User-Agent': random.choice(user_agent_list)
}

class Comment(object):
    def __init__(self, music_id, user_id, content, reply_id, reply_content, liked_count, comment_time):
        self.comment_time = comment_time
        self.liked_count = liked_count
        self.reply_content = reply_content
        self.reply_id = reply_id
        self.music_id = music_id
        self.user_id = user_id
        self.content = content


def get_comment_count(music_id):
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + str(music_id)
    response = requests.post(url, headers=headers)
    json_dict = json.loads(response.content)
    try:
        total = json_dict['total']
    except Exception :
        print(json_dict["message"])
        sys.exit(1)
    return total


def get_comment_by_music_id_and_user_id(music_id, user_id):
    total = get_comment_count(music_id)
    size = 100
    totalPages = math.ceil(total / size)
    i = 0
    for page in range(0, totalPages):
        if totalPages > 20 and (10 < page < totalPages - 10):
            continue
        url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + str(music_id) + '?offset=' + str(
            page * size) + '&limit=' + str(page * size + size)
        response = requests.get(url, headers=headers)
        json_dict = json.loads(response.content)
        # print(json_dict)
        # break
        try:
            comments = json_dict['comments']
        except Exception:
            print(json_dict["message"])
            sys.exit(1)
        for comment in comments:
            is_reply = 1 if len(comment['beReplied']) > 0 else 0
            print(comment)
            if comment['user']['userId'] == user_id or (is_reply == 1
                                                        and comment['beReplied'][0]['user']['userId'] == user_id):
                c = Comment(music_id,
                            comment['user']['userId'],
                            comment['content'],
                            comment['beReplied'][0]['beRepliedCommentId'] if is_reply == 1 else '',
                            comment['beReplied'][0]['content'] if is_reply == 1 else '',
                            comment['likedCount'],
                            datetime.fromtimestamp(comment['time'] / 1000))
                print(c)
                logging.info(comment['content'])
                sql.insert_comment(c)
        i += 1
        print('\r查询成功，歌曲：' + str(music_id) + ',共' + str(total) + '条评论，进度：' + str(i) + '/' + str(
            totalPages if totalPages < 21 else 21),
              end='')
    print(str(music_id) + ",歌曲查找完毕")


def get_comment_by_user_musics(user_id):
    music_list = sql.get_musics_by_user(user_id)
    music_index = 0
    count = len(music_list)
    logging.info('获取成功，共' + str(count) + '首歌曲')
    for music in music_list:
        get_comment_by_music_id_and_user_id(music['music_id'], user_id)
        music_index += 1
        print('\r歌曲:' + str(music['music_id']) + '，查询完毕。进度：' + str(music_index) + '/' + str(count), end='')
        print()


if __name__ == "__main__":
    logging.basicConfig(filename="out.log", level=logging.INFO)
    start = time.time()
    get_comment_by_user_musics(1355997463)
    cost = (time.time() - start)
    print('耗时：' + str(cost) + '秒')
