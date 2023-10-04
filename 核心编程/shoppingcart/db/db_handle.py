import os
import json
from conf import setting

class Serialization:
    def select(self,name):
        path = r'%s/%s.json'%(setting.DB_path,name)

        if os.path.isfile(path):
            with open(path,'rt',encoding='utf-8') as f:
                return json.load(f)

        else:
            return False

    def update(self,user_dic):
        path_file = os.path.join(setting.DB_path,'%s.json'%user_dic['name'])
        # 注册是利用json文件名注册
        with open(path_file, 'wt', encoding='utf-8') as f:
            #  对序列化json文件操dump
            json.dump(user_dic, f)
            # 刷新
            f.flush()



db_serialization=Serialization()
