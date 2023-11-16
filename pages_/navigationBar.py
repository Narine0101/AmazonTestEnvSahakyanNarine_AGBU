from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
from selenium import webdriver

class NavigationBar(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.__cartButtonLocator = (By.ID, "nav-cart-count-container")
        self.__searchBoxLocator = (By.XPATH, "//input[@id='twotabsearchtextbox']")
        self.__searchSubmitLocator = (By.XPATH, "//div[@class = 'nav-search-submit nav-sprite']")

    def click_to_cart_button(self):
        cardButtonElement = self._find_element(self.__cartButtonLocator)
        self._click(cardButtonElement)

    def fill_search_field(self):
        searchBoxElement = self.driver.find_element(self.__searchBoxLocator)
        self._fill_field(searchBoxElement, "paper towels rolls")

    def click_to_nav_search_submit(self):
        searchSubmitElement = self.driver.find_element(self.__searchSubmitLocator)
        self._click(searchSubmitElement)


