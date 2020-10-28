from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click(self, location):
        self.find_element(location).click()

    def input(self, location, text):
        self.find_element(location).send_keys(text)

    def find_element(self, location):
        by = location[0]
        value = location[1]
        if by == By.XPATH:
            return WebDriverWait(self.driver, 5, 1).until(
                lambda x: x.find_element(by, self.make_xpath(value)))
        else:
            return WebDriverWait(self.driver, 5, 1).until(
                lambda x: x.find_element(by, value))

    def make_one_xpath(self, loc):
        loc_list = loc.split(",")
        key_index = 0
        value_index = 1
        option_index = 2
        result = ""
        if len(loc_list) == 3:
            if loc_list[option_index] == "1":
                result = "contains(@{},'{}')".format(loc_list[key_index], loc_list[value_index])
            else:
                result = "@{}='{}'".format(loc_list[key_index], loc_list[value_index])
        elif len(loc_list) == 2:
            result = "@{}='{}'".format(loc_list[key_index], loc_list[value_index])
        return result

    def make_xpath(self, loc):
        result = ""
        if isinstance(loc, str):
            # 如果是正常的xpath：
            if loc.startswith("//"):
                return loc
            # 如果是自己的格式：
            else:
                return "//*[]".format(self.make_one_xpath(loc))
        else:
            for i in loc:
                result += (self.make_one_xpath(i) + "and")
            return "//*[{}]".format(result.rstrip("and"))
