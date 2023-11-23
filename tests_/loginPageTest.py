import time
from pages_.loginPage import LoginPage
from testData_.testData import validUser, userWithInvalidPassword, userWithInvalidUserName, signInPageUrl
from tests_.baseTest import BaseTestWithoutLogin


class LogIn(BaseTestWithoutLogin):

    def test_positive_login(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(validUser.userName)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(validUser.password)
        time.sleep(7)
        loginPageObj.click_to_keep_me_signed_in_check_box()
        time.sleep(1)
        loginPageObj.click_to_signin_button()
        time.sleep(5)
        self.assertEqual("Amazon.com. Spend less. Smile more.", loginPageObj._get_title())

    def test_negative_login_with_invalid_password(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(userWithInvalidPassword.userName)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(userWithInvalidPassword.password)
        time.sleep(7)
        loginPageObj.click_to_keep_me_signed_in_check_box()
        time.sleep(1)
        loginPageObj.click_to_signin_button()
        time.sleep(5)
        self.assertEqual("Your password is incorrect", loginPageObj.get_incorrect_password_error_message_text())

    def test_negative_login_with_invalid_email(self):
        self.driver.get(signInPageUrl)
        loginPageObj = LoginPage(self.driver)
        loginPageObj.fill_username_field(userWithInvalidUserName.userName)
        loginPageObj.validate_continue_button_text()
        loginPageObj.click_to_continue_button()
        self.assertEqual("We cannot find an account with that email address", loginPageObj.get_incorrect_email_error_message_text())

    def test_sign_out_login(self):
        self.driver.get(signInPageUrl)
        time.sleep(7)
        loginPageObj = LoginPage(self.driver)
        time.sleep(7)
        loginPageObj.fill_username_field(validUser.userName)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(validUser.password)
        time.sleep(6)
        loginPageObj.click_to_keep_me_signed_in_check_box()
        time.sleep(1)
        loginPageObj.click_to_signin_button()
        time.sleep(5)
        self.assertEqual("Amazon.com. Spend less. Smile more.", loginPageObj._get_title())
        loginPageObj.mouse_move_to_account_element()
        time.sleep(2)
        loginPageObj.click_to_sign_out_button()
        time.sleep(2)
        self.assertEqual("Amazon Sign-In", loginPageObj._get_title())

