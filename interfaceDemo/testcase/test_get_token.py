import requests

def test_token():
    corpid="wwd6fc5a5c802ec799"
    corpsecret="N6nw0IQVwBfdLASfXem2OohB6WyMahaaGCaMYbrTaU8"
    url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+corpid+"&corpsecret="+corpsecret
   #设置代理
    myproxies = {
        'http':'192.168.0.106:8889',
        'https': '192.168.0.106:8889',
    }
    #使用代理，可以在本地代理上查看到接口的请求数据
    res=requests.get(url,proxies=myproxies,verify=False)
    print(res.json())
    qiye_token=res.json().get("access_token")
    return qiye_token
