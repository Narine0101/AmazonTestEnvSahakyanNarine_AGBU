import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class LogIn(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(
            "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")


    def test_positive_login(self):


        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("narine.narine.1962@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("Sahakyan1963!")
        time.sleep(7)
        loginPageObj.click_to_signin_button()
        time.sleep(5)

    # def test_negative_login(self):
    #     loginPageObj = LoginPage(self.driver)
    #     loginPageObj.fill_username_field("narine.narine.19621@mail.ru")
    #     # loginPageObj.validate_continue_button_text()
    #     loginPageObj.click_to_continue_button()
    #     loginPageObj.fill_password_field("asdfg")
    #     loginPageObj.click_to_signin_button()
    #
    #     self.assertEqual("Amazon.com. Spend less. Smile more.", self.driver.title)

    def tearDown(self):
        self.driver.close()

