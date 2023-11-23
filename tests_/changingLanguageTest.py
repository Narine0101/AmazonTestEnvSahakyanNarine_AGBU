import time
from pages_.languageSettingsPage import LanguageSetings
from pages_.navigationBar import NavigationBar
from tests_.baseTest import BaseTestWithoutLogin


class LanguageSet(BaseTestWithoutLogin):

    def test_changing_language_to_spanish(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_on_language_changing_button()
        time.sleep(5)
        languageSettingsObj = LanguageSetings(self.driver)
        languageSettingsObj.select_spanish_language_button()
        time.sleep(5)
        languageSettingsObj.click_on_save_change_button()
        time.sleep(5)

        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.validate_language_button_text()


