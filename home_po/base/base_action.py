from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, location):
        self.find_element(location).click()

    def input(self, location, text):
        self.find_element(location).send_keys(text)

    def find_element(self, location):
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(location[0], location[1]))
