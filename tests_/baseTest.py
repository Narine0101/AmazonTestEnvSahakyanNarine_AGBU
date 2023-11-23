import time
import unittest
from selenium import webdriver
from pages_.loginPage import LoginPage
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from testData_.testData import validUser, signInPageUrl, mainPageUrl


class BaseTestWithoutLogin(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Firefox()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(mainPageUrl)

    def tearDown(self):
        self.driver.close()


class BaseTestWithLogin(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Firefox()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get(signInPageUrl)

        self.loginPageObj = LoginPage(self.driver)
        self.loginPageObj.fill_username_field(validUser.userName)
        self.loginPageObj.click_to_continue_button()
        self.loginPageObj.fill_password_field(validUser.password)
        time.sleep(7)
        self.loginPageObj.click_to_signin_button()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
