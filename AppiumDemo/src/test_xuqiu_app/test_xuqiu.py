# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

#实战：打开模拟器，搜索拼多多股票

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "demo"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
#解决权限问题
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#隐式等待
driver.implicitly_wait(5)


el5 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el6.click()
el6.send_keys("pdd")
el6.click()

#退出
# driver.quit()