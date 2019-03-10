#搜索股票，并点击拼多多股票，进入股票详情
#以pytest编写最佳

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import time

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "demo"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.xueqiu.android:id/open")
el1.click()
el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el2.click()
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/agree")
el3.click()
el4 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el4.click()
el5 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el6.click()
el6.send_keys("pdd")
el6.click()
el7 = driver.find_element_by_xpath("//*[@text='拼多多']").click()
# el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]")

#driver.quit()