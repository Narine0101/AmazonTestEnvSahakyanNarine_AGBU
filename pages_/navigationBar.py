from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from selenium import webdriver


class NavigationBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__searchFieldLocator = (By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = (By.ID, "nav-search-submit-button")
        self.__cartButtonLocator = (By.ID, "nav-cart")
        self.__languageChangingButtonLocator = (By.CLASS_NAME, "icp-nav-link-inner")
        self.__languageButtonTextLocator = (By.XPATH, "//a[@id = 'icp-nav-flyout']/span/span[2]/div")
        self.__searchSubmitLocator = (By.XPATH, "//div[@class = 'nav-search-submit nav-sprite']")

    def click_on_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click(searchButtonElement)

    def click_on_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click(cartButtonElement)

    def click_on_language_changing_button(self):
        languageChangingButtonElement = self._find_element(self.__languageChangingButtonLocator)
        self._click(languageChangingButtonElement)

    def fill_in_search_field(self, text):
        searchFieldElement = self.driver.find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, text)

    def validate_language_button_text(self):
        languageButtonTextElement = self._find_element(self.__languageButtonTextLocator)
        if self._get_element_text(languageButtonTextElement) != "ES":
            print("Error: The language is not changed")
            exit(3)

    def click_on_nav_search_submit(self):
        searchSubmitElement = self.driver.find_element(self.__searchSubmitLocator)
        self._click(searchSubmitElement)


