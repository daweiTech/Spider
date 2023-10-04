import time
from conf import setting

def log(msg):
    current_time = time.strftime('%Y-%m-%d %X')
    with open(setting.LOG1_path, 'a', encoding='utf-8') as f:
        f.write(current_time + '-' * 5 + msg + '\n')