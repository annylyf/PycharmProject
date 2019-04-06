import requests

def test_token():
    url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwd6fc5a5c802ec799&corpsecret=N6nw0IQVwBfdLASfXem2OohB6WyMahaaGCaMYbrTaU8"
    res=requests.get(url)
    print(res.json())
    qiye_token=res.json().get("access_token")
    return qiye_token
