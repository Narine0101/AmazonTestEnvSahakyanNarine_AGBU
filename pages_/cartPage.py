from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__firstProductDeleteButtonLocator = (By.XPATH, "(//input[@value='Delete'])[1]")

    def delete_firstProduct_from_cart(self):
        firstProductDeleteButtonElement = self._find_element(self.__firstProductDeleteButtonLocator)
        self._click(firstProductDeleteButtonElement)




