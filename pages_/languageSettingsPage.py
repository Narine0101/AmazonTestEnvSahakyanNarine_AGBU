from selenium.webdriver.common.by import By
from selenium import webdriver
from pages_.basePage import BasePage


class LanguageSetings(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self.__spanishLanguageButtonLocator = (By.XPATH, "//div[@id = 'icp-language-settings']/div[3]/div/label/span/span")
        self.__spanishLanguageButtonLocator = (By.XPATH, "//input[@value = 'es_US']/../..")
        self.__saveChangesButtonLocator = (By.CLASS_NAME, "a-button-input")

    def select_spanish_language_button(self):
        spanishLanguageButtonElement = self._find_element(self.__spanishLanguageButtonLocator)
        self._click(spanishLanguageButtonElement)

    def click_on_save_change_button(self):
        saveChangesButtonElement = self._find_element(self.__saveChangesButtonLocator)
        self._click(saveChangesButtonElement)