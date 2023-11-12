from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__cartButtonLocator = (By.ID, "nav-cart-count-container")
        self.__searchbuttonLocator = (By.XPATH, "//input[@placeholder = 'Search Amazon']")
        self.__searchBoxLocator = (By.XPATH, "//input[@placeholder = 'Search Amazon']")
        self.__searchSubmitLocator = (By.XPATH, "//div[@class = 'nav-search-submit nav-sprite']")

    def click_to_cart_button(self):
        cardbuttonElement = self._find_element(self.__cartButtonLocator)
        self._click(cardbuttonElement)

    def click_to_search_button(self):
        searchbuttonElement = self.driver.find_element(self.__searchbuttonLocator)
        self._click(searchbuttonElement)

    def send_text_to_search_box(self):
        searchBoxElement = self.driver.find_element(self.__searchBoxLocator)
        self._fill_field(searchBoxElement, "paper towels rolls")

    def click_to_nav_search_submit(self):
        searchSubmitElement = self.driver.find_element(self.__searchSubmitLocator)
        self._click(searchSubmitElement)


