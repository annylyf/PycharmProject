#用账号密码的方式登录
#检查登录是否成功
#用pytest自动化测试框架

from selenium import webdriver
import time

def test_login_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.douban.com/")
    time.sleep(10)

    #切换frame
    login_frame = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(login_frame)

    password_login = driver.find_element_by_class_name('account-tab-account')
    password_login.click()

    user_name = driver.find_element_by_id('username')
    user_name.send_keys("17666137620")
    pass_name = driver.find_element_by_id('password')
    pass_name.send_keys("lyf1024")

    elements = driver.find_element_by_link_text("登录豆瓣")
    elements.click()

    #断言成功
    assert driver.title == "豆瓣"





