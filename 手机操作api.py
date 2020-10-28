from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}

desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1.2"
desired_caps["deviceName"] = "emulator-5558"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"
desired_caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# 获取当前时间
print(driver.device_time)
# 获取手机分辨率
print(driver.get_window_size())

while True:
    try:
        driver.find_element_by_xpath("//*[contains(@text,'关于平板电脑')]").click()
        break
    except Exception:
        window_width = driver.get_window_size()["width"]
        window_height = driver.get_window_size()["height"]
        start_x = window_width * 0.5
        end_x = start_x
        end_y = window_height * 0.25
        start_y = end_y * 3
        driver.swipe(start_x, start_y, end_x, end_y, 5000)
