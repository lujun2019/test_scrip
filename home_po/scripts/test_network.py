import sys, os

sys.path.append(os.getcwd())
from base.base_driver import get_driver
from page.network_page import NetworkPage


class TestNetwork:
    def setup(self):
        self.driver = get_driver()
        self.driver = NetworkPage(self.driver)

    def test_network_2g(self):
        self.driver.click_more()
        self.driver.click_mobile_network()
        self.driver.click_network_size()
        self.driver.click_network_2g()

    def test_network_3g(self):
        self.driver.click_more()
        self.driver.click_mobile_network()
        self.driver.click_network_size()
        self.driver.click_network_3g()
