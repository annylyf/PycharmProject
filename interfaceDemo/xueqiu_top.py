#通过python requests访问接口的方式获取https://xueqiu.com/hq ;页面的涨跌幅榜的股票。
#requests.get(url)
#第一步：需要知道是哪个接口
#GET /service/v5/stock/screener/quote/list?type=sha&order_by=percent&order=desc&size=10&page=1&_=1553413575932 HTTP/1.1
#第二步：分析接口参数，headers的特征
#Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
#第三步：通过requests访问接口，要访问成功需要带入参数，headers
#_cookie：ga=GA1.2.604562630.1551074303; device_id=6e4492f158265b8f796eeef99c12fcdc; aliyungf_tc=AQAAAJhP+SerRw4AUGP7Z6f4XEt04svY; xq_a_token=c9621956cf4a7c4f938b1556f00b48f4d719365c; xq_a_token.sig=WPZNprUeyGC1XxlQpDKDDcpd-i8; xq_r_token=843932e531acb61163845ae7ce15e4f2d4024790; xq_r_token.sig=J-wCiH73Aa4h8WossmGbm0oisW4; u=541553397069674; Hm_lvt_1db88642e346389874251b5a1eded6e3=1551074303,1551074341,1553397070; _gid=GA1.2.1266147437.1553398843; s=dy112lr63d; __utma=1.604562630.1551074303.1553412432.1553412432.1; __utmc=1; __utmz=1.1553412432.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1553413568; __utmb=1.8.10.1553412432


import requests
myheaders = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url='https://xueqiu.com/hq#type=sha&exchange=CN&firstName=%E6%B2%AA%E6%B7%B1%E8%82%A1%E5%B8%82&secondName=%E6%8E%92%E8%A1%8C&market=CN&order=desc&order_by=percent&plate=%E6%B2%AAA%E6%B6%A8%E5%B9%85%E6%A6%9C'
res=requests.get(url,verify=False,headers=myheaders)
print(res.json())
print('*'*200)
print(res.text)
print('*'*200)
print(res.content)



