from selenium.webdriver.common.by import By
from selenium import webdriver
from pages_.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Firefox):
        super().__init__(driver)
        self.__usernameFieldLocator = (By.ID, "ap_email")
        self.__continueButtonLocator = (By.ID, "continue")
        self.__passwordFieldLocator = (By.ID, "ap_password")
        self.__signInButtonLocator = (By.ID, "signInSubmit")
        self.__incorrectPasswordErrorMessageTextLocator = (By.CLASS_NAME, "a-list-item")
        self.__incorrectEmailErrorMessageTextLocator = (By.CLASS_NAME, "a-list-item")
        self.__keepMeSignedInLocator = (By.XPATH, "//input[@name = 'rememberMe']")

    def fill_username_field(self, username):
        userNameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(userNameFieldElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_to_signin_button(self):
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        self._click(signInButtonElement)

    def get_incorrect_password_error_message_text(self):
        incorrectPasswordErrorMessageTextElement = self._find_element(self.__incorrectPasswordErrorMessageTextLocator)
        return self._get_element_text(incorrectPasswordErrorMessageTextElement)

    def get_incorrect_email_error_message_text(self):
        incorrectEmailErrorMessageTextElement = self._find_element(self.__incorrectEmailErrorMessageTextLocator)
        return self._get_element_text(incorrectEmailErrorMessageTextElement)

    def validate_continue_button_text(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        if self._get_element_text(continueButtonElement) != "Continue":
            print("Error: Wrong continue button text")
            exit(2)

    def click_to_keep_me_signed_in_check_box(self):
        keepMeSignedInElement = self._find_element(self.__keepMeSignedInLocator)
        self._click(keepMeSignedInElement)
