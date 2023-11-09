from selenium.webdriver.common.by import By


class DuckDuckGoBangsPage:

    # URL
    MAIN_URL = "https://duckduckgo.com/bangs"

    # Locators
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BTN = (By.XPATH, "//button[contains(@class, 'searchbox_searchButton')]")
    WIKIPEDIA_LINK = (By.XPATH, "//*[text()='!w filter bubble']")
    ROOT_LINK = (By.XPATH, "//*[text()='our geek roots']")
    BANG_LINK = (By.XPATH, "//*[text()='submit your own']")
    SUGGESTION_LINK = (By.XPATH, "//*[text()='Make a suggestion!']")
    SEARCH_BANGS_INPUT = (By.XPATH, "//input[@class='input_input___QXpk']")
    RESULT_LINKS = (By.XPATH, "//ul[@id='bangs-lists']")
    ALL_RESULT_BTN = (By.XPATH, "//button[contains(@class, 'bangsBrowser_showAll')]")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load_main(self):
        self.browser.get(self.MAIN_URL)

    def title(self):
        return self.browser.title

    def url(self):
        return self.browser.current_url

    def get_search_input_text(self):
        search_text = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_text.get_attribute("placeholder")
        return value

    def search_text(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)

    def search_click(self):
        search_button = self.browser.find_element(*self.SEARCH_BTN)
        search_button.click()

    def wikipedia_link_click(self):
        wikipedia_link = self.browser.find_element(self.WIKIPEDIA_LINK)
        wikipedia_link.click()

    def root_link_click(self):
        root_link = self.browser.find_element(self.ROOT_LINK)
        root_link.click()

    def bang_link_click(self):
        bang_link = self.browser.find_element(self.BANG_LINK)
        bang_link.click()

    def suggestion_link_click(self):
        suggestion_link = self.browser.find_element(self.SUGGESTION_LINK)
        suggestion_link.click()

    def search_bangs_attribute(self):
        search_bangs = self.browser.find_element(*self.SEARCH_BANGS_INPUT)
        value = search_bangs.get_attribute("placeholder")
        return value

    def search_bangs_input(self, bangs):
        bangs_input = self.browser.find_element(*self.SEARCH_BANGS_INPUT)
        bangs_input.send_keys(bangs)

    def result_click(self):
        bangs_results = self.browser.find_element(*self.RESULT_LINKS)

    def all_result_click(self):
        all_result = self.browser.find_element(*self.ALL_RESULT_BTN)
        all_result.click()
