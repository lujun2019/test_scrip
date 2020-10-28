import pytest, os, sys

sys.path.append(os.getcwd())
from appium import webdriver
from base.base_driver import get_driver
from page.display_page import DisplayPage


class TestDisplay:

    def setup(self):
        self.driver = get_driver()
        self.driver = DisplayPage(self.driver)

    def test_mobile_display_input(self):
        self.driver.click_search()
        self.driver.send_text("hello")
        self.driver.click_back()
