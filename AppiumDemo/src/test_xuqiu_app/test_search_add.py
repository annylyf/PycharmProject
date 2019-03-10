#进去自选，点击搜索，搜索alibaba，点击添加，回到自选，判断阿里巴巴已经在自选中

import pytest
import unittest
from appium import webdriver

class Test_xueqiu(unittest.TestCase):

    def test_base(self):
        print("setUp")
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决权限问题,在测试过程中可以解决遇到的权限问题
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(6)


    def test_search_alibaba(self):
        # 多次定位(需要等待页面已经加载完成，但是并不能准确知道已经加载完成)
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id,'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id,'tab_name')]")
        self.driver.find_element_by_xpath(
            "//*[@text='自选' and contains(@resource-id,'tab_name')]").click()
        self.driver.find_element_by_id("action_create_cube").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
        if len(self.driver.find_elements_by_id("follow_btn")) > 0:
            self.driver.find_element_by_id("follow_btn").click()

        self.driver.find_elements_by_id("action_close").click()

        assert 1==len(self.driver.find_elements_by_xpath(
            "//*[contains(@resource-id,'portfolio_stockName') and @text='阿里巴巴']"))





