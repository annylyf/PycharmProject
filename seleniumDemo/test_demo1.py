from unittest import TestCase

from selenium import webdriver

class TestBrowser(TestCase):
    def test_chrome(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://baidu.com")
        print(self.driver.page_source)

