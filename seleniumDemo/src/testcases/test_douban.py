
from selenium import webdriver
import time

def test_douban_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.douban.com/")
    time.sleep(10)
    #切换frame
    login_frame = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(login_frame)
    #存在唯一的class_name
    forget_password_ele = driver.find_element_by_class_name("account-form-link")
    forget_password_ele.click()

    #返回所有的windows handles
    open_windows = driver.window_handles
    print("windows: "+str(open_windows))
    #动态获取Windows的名字
    driver.switch_to.window(open_windows[1])

    #验证用例是否正确
    assert driver.title == '帐号 使用帮助'
    time.sleep(10)
    print("End")