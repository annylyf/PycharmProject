
import requests
import logging
from testcase import test_get_token
def test_send_msg():
    # ACCESS_TOKE = "7Yb_a7gQ-XzBH54_aJ-wWvn-nk7DUc1zRU5gM_WqZ5xp-D921QqWZjlPvO7Pb_e5RE9a7CTyvr8OEauEpgE7pqEIYjwXzELNDSD1W2tZo2T0wnVdbO0IoKiVlj9Ji2Jcs4YjJAQMKH-hlNcUyEVyUr0QiPm2PZJgvLIbzVg1nQKojxOC9Hw4d9pJHLoA63WESmm_A08CLtYKKd5BNFT0YQ"
    ACCESS_TOKE=test_get_token.test_token()
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+ACCESS_TOKE
    send_json = {
   "touser" : "LiaoYanFang",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   "msgtype" : "text",
   "agentid" : 1000002,
   "text" : {
       "content" : "Anny测试消息"
   },
   "safe":0
    }

    res = requests.post(url,json=send_json)
    assert res.json().get('errmsg') == 'ok'
    print(res.json())

def test_send_msg2():
    # ACCESS_TOKE = "7Yb_a7gQ-XzBH54_aJ-wWvn-nk7DUc1zRU5gM_WqZ5xp-D921QqWZjlPvO7Pb_e5RE9a7CTyvr8OEauEpgE7pqEIYjwXzELNDSD1W2tZo2T0wnVdbO0IoKiVlj9Ji2Jcs4YjJAQMKH-hlNcUyEVyUr0QiPm2PZJgvLIbzVg1nQKojxOC9Hw4d9pJHLoA63WESmm_A08CLtYKKd5BNFT0YQ"
    ACCESS_TOKE=test_get_token.test_token()
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+ACCESS_TOKE
    send_json = {
   "touser" : "LiaoYanFang",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   # "msgtype" : "text",
   "agentid" : 1000002,
   "text" : {
       "content" : "Anny测试消息"
   },
   "safe":0
    }

    res = requests.post(url,json=send_json)
    assert 'invalid message type' in res.json().get('errmsg')
    print(res.json())