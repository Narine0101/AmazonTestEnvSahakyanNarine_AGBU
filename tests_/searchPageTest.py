import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from pages_.navigationBar import NavigationBar
from pages_.resultPage import ResultPage
from pages_.productDetails import ProductDetails
from pages_.cartPage import CartPage


class SearchPage(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Firefox()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        self.loginPageObj = LoginPage(self.driver)
        self.loginPageObj.fill_username_field("narine.narine.1962@mail.ru")
        self.loginPageObj.click_to_continue_button()
        self.loginPageObj.fill_password_field("Sahakyan1963!")
        time.sleep(7)
        self.loginPageObj.click_to_signin_button()
        time.sleep(5)

    def test_search_product(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_in_search_field("Christmas tree")
        navigationBarObj.click_on_search_button()

        resultPageObj = ResultPage(self.driver)
        resultPageObj.click_on_sort_by_button()
        resultPageObj.click_on_best_sellers_button()
        resultPageObj.click_on_first_product_from_list()

        productDetailsObj = ProductDetails(self.driver)
        cartPageObj = CartPage(self.driver)
        cartPreviousElement = cartPageObj.get_cart_count_element()
        productDetailsObj.click_on_add_to_cart_button()
        cartCurrentElement = cartPageObj.get_cart_count_element()
        self.assertEqual(cartPreviousElement+1, cartCurrentElement)

    def tearDown(self):
        self.driver.close()




