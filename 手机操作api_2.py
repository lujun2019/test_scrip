from appium import webdriver
from time import sleep
from appium.webdriver.connectiontype import ConnectionType

desired_caps = {}

desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1.2"
desired_caps["deviceName"] = "emulator-5558"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"
desired_caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# 音量加
# for i in range(3):
#     driver.keyevent(24)

# sleep(3)
# driver.keyevent(25)

# 打开通知栏
# driver.open_notifications()
# 关闭通知栏
# driver.back()

# 获取当前网络
# print(driver.network_connection)
# driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)

# 截图
driver.get_screenshot_as_file("./xxx.png")