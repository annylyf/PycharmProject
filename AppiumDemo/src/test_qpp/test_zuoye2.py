#点击自选，点击其他股票，搜索alibaba，点击加入，再点击取消，验证allibaba已在自选股中
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

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
el5 = driver.find_element_by_xpath("//*[@text='自选']")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/action_create_cube")
el6.click()
el7 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el7.click()
el7.send_keys("alibaba")
el7.click()
el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView")
el8.click()
el9 = driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultNegative")
el9.click()
el10 = driver.find_element_by_id("com.xueqiu.android:id/action_close")
el10.click()
el11 = driver.find_element_by_id("com.xueqiu.android:id/iv_close")
el11.click()

driver.quit()