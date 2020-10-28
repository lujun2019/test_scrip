import os, sys, pytest

sys.path.append(os.getcwd())
from base.base_driver import get_driver
from page.search_page import SearchPage
from base.base_yaml import get_yaml_as_file_name


def data_with_key(key):
    return get_yaml_as_file_name("search_data")[key]


class TestSearch:
    def setup(self):
        self.driver = get_driver()
        self.driver = SearchPage(self.driver)

    @pytest.mark.parametrize("contains", data_with_key("test_search_input"))
    def test_search_input(self, contains):
        self.driver.click_search()
        self.driver.input_message(contains)
        self.driver.click_back()
