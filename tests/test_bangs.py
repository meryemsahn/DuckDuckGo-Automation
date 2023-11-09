import pytest
from pages.bangs import DuckDuckGoBangsPage


class TestBangsPage:

    @pytest.fixture(autouse = True)
    def class_setup(self, browser):
        # Given the DuckDuckGoBang home page is displayed
        self.bangs_page = DuckDuckGoBangsPage(browser)
        self.bangs_page.load_main()

    def test_check_input_attribute(self):
        # Then get input attribute of the search
        attribute = self.bangs_page.get_search_input_text()

        # And make sure that the attribute is correct
        assert attribute == "Search without being tracked"


