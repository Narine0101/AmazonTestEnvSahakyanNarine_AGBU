import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.languageSettingsPage import LanguageSetings
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener


class LanguageSet(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Firefox()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field("narine.narine.1962@mail.ru")
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field("Sahakyan1963!")
        time.sleep(7)
        loginPageObj.click_to_signin_button()

        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_on_language_changing_button()
        time.sleep(5)

    def test_changing_language_to_spanish(self):
        languageSettingsObj = LanguageSetings(self.driver)
        languageSettingsObj.select_spanish_language_button()
        time.sleep(5)
        languageSettingsObj.click_on_save_change_button()
        time.sleep(5)

        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.validate_language_button_text()

    def tearDown(self):
        self.driver.quit()
