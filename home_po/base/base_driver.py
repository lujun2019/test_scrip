from appium import webdriver


def get_driver():
    desired_caps = {}

    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "5.1"
    desired_caps["deviceName"] = "192.168.34.101:5555"
    desired_caps["appPackage"] = "com.android.settings"
    desired_caps["appActivity"] = ".Settings"
    desired_caps["noReset"] = True
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver
