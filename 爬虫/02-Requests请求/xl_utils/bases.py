# from retrying import retry
import requests
from retrying import retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from lxml import html
etree = html.etree
import random,time

#https://diag.qichacha.com/  浏览器信息

class FakeChromeUA:
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
                '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)','(Macintosh; Intel Mac OS X 10_12_6)'
               ]

    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    @classmethod
    def get_ua(cls):
        return ' '.join(['Mozilla/5.0', random.choice(cls.os_type), 'AppleWebKit/537.36','(KHTML, like Gecko)', cls.chrome_version, 'Safari/537.36'])


class Spiders(FakeChromeUA):
    urls = []
    @retry(stop_max_attempt_number=3, wait_fixed=2000)
    def fetch(self, url, param=None,headers=None):
        try:
            if not headers:
                headers ={}
                headers['user-agent'] = self.get_ua()
            else:
                headers['user-agent'] = self.get_ua()
            self.wait_some_time()
            response = requests.get(url, params=param,headers=headers)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response
        except requests.ConnectionError:
            return

    def wait_some_time(self):
        time.sleep(random.randint(100, 300) / 1000)