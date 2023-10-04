import httpx
import os

class Spider():
    def __init__(self):
        pass

    def url_list(self):
        url = [ 'https://pic.netbian.com/uploads/allimg/220211/004115-1644511275bc26.jpg',

                'https://pic.netbian.com/uploads/allimg/220215/233510-16449393101c46.jpg',

                'https://pic.netbian.com/uploads/allimg/211120/005250-1637340770807b.jpg']
        return url

    def saveImg(self,index,byte):
        if os.path.exists("./image") is False:
            os.mkdir('./image')
        with open('./image/{}.jpg'.format(str(index)), 'wb') as f:
            f.write(byte)

    def crawler(self):
        urllist = self.url_list()
        for index,u in enumerate(urllist):
            data = httpx.get(u)
            self.saveImg(index,data.content)

if __name__ == '__main__':
    Spider().crawler()
