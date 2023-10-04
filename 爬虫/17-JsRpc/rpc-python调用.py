import requests

def demo():

    data = {"group": "rpc-test",
            "action": "clientTime",
            "pwd":'123123'
            }


def get_cookie():
    data = {"group": "rpc-test",
            "action": "gc",
            }
    res = requests.get("http://127.0.0.1:5620/business-demo/invoke",params=data )
    print(res.text)

get_cookie()