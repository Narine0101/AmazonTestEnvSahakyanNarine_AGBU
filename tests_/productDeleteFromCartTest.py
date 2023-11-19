import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.cartPage import CartPage
from pages_.navigationBar import NavigationBar
from pages_.languageSettingsPage import LanguageSetings
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class ProductDeletion(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Firefox()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("narine.narine.1962@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("Sahakyan1963!")
        time.sleep(7)
        loginPageObj.click_to_signin_button()

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

    def tearDown(self):
        self.driver.quit()

