import requests
#ssr配置代理
proxies={'http': 'http://198.49.68.80:80', 'https': 'http://198.49.68.80:80'}
r = requests.get('https://www.google.com/',proxies=proxies)
print(r.status_code)
