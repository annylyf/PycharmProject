
import requests
from testcase import test_get_token
import logging

def test_upload_image():
    # ACCESS_TOKE = "7Gwqo0iuit2c1uMkfgLwEIoImfK6pDTZI18wFqt-1bzo7NeFiibPfQa5UbpDnt6FYQzf5CbhUV5Ea8be3UtruS_wBk-Igp6Wihj95a0ZVl9jFMbboWLG0FpVaQqE1At3PvBnDGtEG6vgPbC7waoK_r9_fOALFLkjoT5gZQMSL0zYfFM7A8y5gmid6vw_3huoOnt4Zzw9nux9T1pUH5V4vg"
    #使用动态的token
    ACCESS_TOKE=test_get_token.test_token()
    url="https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token="+ACCESS_TOKE
    upload_file = {'media':('you.jpg',open('you.jpg','rb'),'image/jpg')}
    #发送post请求，将请求结果赋值到res
    res=requests.post(url,files=upload_file,proxies=)
    #断言，测试返回结果是否符合预期
    assert res.json().get('errcode')==0
    logging.debug("debug message")
    media_id=res.json().get('media_id')
    print(media_id)
    print(res.json())
