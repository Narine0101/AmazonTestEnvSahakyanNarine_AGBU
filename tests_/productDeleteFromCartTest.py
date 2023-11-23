import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.cartPage import CartPage
from pages_.navigationBar import NavigationBar
from pages_.languageSettingsPage import LanguageSetings
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
import time
from pages_.languageSettingsPage import LanguageSetings
from pages_.navigationBar import NavigationBar
from tests_.baseTest import BaseTestWithLogin


class ProductDeletion(BaseTestWithLogin):

    def test_for_empty_cart_page(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_on_cart_button()

        cartPageObj = CartPage(self.driver)
        cartPageObj.validate_emptiness_of_cart()

    def test_delete_first_product(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_on_cart_button()

        cartPageObj = CartPage(self.driver)
        cartCountBeforeDelete = cartPageObj.get_cart_count_element()
        cartPageObj.delete_first_product_from_cart()
        cartCountAfterDelete = cartPageObj.get_cart_count_element()

        self.assertEqual(cartCountBeforeDelete-1, cartCountAfterDelete)

    def test_for_deleting_all_products(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_on_cart_button()

        cartPageObj = CartPage(self.driver)
        cartCountBeforeDelete = cartPageObj.get_cart_count_element()
        while cartCountBeforeDelete != 0:
            cartPageObj.delete_first_product_from_cart()
            cartCountBeforeDelete -= 1


