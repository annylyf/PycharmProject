
import requests

def test_upload_image():
    ACCESS_TOKE = "7Gwqo0iuit2c1uMkfgLwEIoImfK6pDTZI18wFqt-1bzo7NeFiibPfQa5UbpDnt6FYQzf5CbhUV5Ea8be3UtruS_wBk-Igp6Wihj95a0ZVl9jFMbboWLG0FpVaQqE1At3PvBnDGtEG6vgPbC7waoK_r9_fOALFLkjoT5gZQMSL0zYfFM7A8y5gmid6vw_3huoOnt4Zzw9nux9T1pUH5V4vg"
    url="https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token="+ACCESS_TOKE
    upload_file = {'media':('1111.jpg',open('1111.jpg','rb'),'image/jpg')}
    res=requests.post(url,files=upload_file)
    assert res.json().get('errcode')==0
    print(res.json())