from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_.utilities_.customLogger import *


class BasePage():
    def __init__(self, driver: webdriver.Firefox):
        self.driver = driver

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            logger("INFO", f"The locator of element is found successfully: {locator}")
            return element
        except:
            logger("ERROR", f"The element by locator: {locator} not found")
            exit(1)

    def _click(self, element):
        element.click()
        logger("INFO", f"The click is done on the webElement: {element}")

    def _fill_field(self, element, text):
        element.clear()
        element.send_keys(text)
        logger("INFO", f"The text {text} is successfully added to webElement: {element}")

    def _get_title(self):
        logger("INFO", f"The title  is found successfully: {self.driver.title}")
        return self.driver.title

    def _get_element_text(self, element):
        logger("INFO", f"The text is founded: {element.text}")
        return element.text

