import pytest
import unittest
from appium import webdriver
import time


class TestXueqiu(unittest.TestCase):

    def setUp(self):
        print("setUp")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决权限问题,在测试过程中可以解决遇到的权限问题
        caps["autoGrantPermissions"] = "true"
        
        if self.driver!=None:
            caps["noReset"]="true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(10)

    def test_add_stock(self):
        self.driver.find_element_by_id("tv_search").click()
        #打印页面元素
        # print(self.driver.page_source)
        self.driver.find_element_by_id("search_input_text").send_keys("pdd")
        #判断元素是否存在
        if len(self.driver.find_elements_by_id("follow_btn")) > 0:
            self.driver.find_element_by_id("follow_btn").click()
            #使用xpath定位方式
            self.driver.find_element_by_xpath("//*[@text='下次再说']").click()

    def test_check_stock(self):
        #多次定位(需要等待页面已经加载完成，但是并不能准确知道已经加载完成)
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id,'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id,'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id,'tab_name')]").click()
        assert 1==len(self.driver.find_elements_by_xpath(
            "//*[contains(@resource-id,'portfolio_stockName') and @text='拼多多']"))
