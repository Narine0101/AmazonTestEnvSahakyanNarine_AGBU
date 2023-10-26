from selenium.webdriver.common.by import By


class NavigationBar():
    def __init__(self, driver):
        self.driver = driver

    def click_to_cart_button(self):
        cardbuttonElement = self.driver.find_element(By.ID, "nav-cart-count-container")
        cardbuttonElement.click()

    def click_to_search_button(self):
        searchbuttonElement = self.driver.find_element(By.XPATH, "//input[@placeholder = 'Search Amazon']")
        searchbuttonElement.click()

    def send_text_to_search_box(self):
        searchBoxElement = self.driver.find_element(By.XPATH, "//input[@placeholder = 'Search Amazon']")
        searchBoxElement.send_keys("paper towels rolls")

    def click_to_nav_search_submit(self):
        searchSubmitElement = self.driver.find_element(By.XPATH, "//div[@class = 'nav-search-submit nav-sprite']")
        searchSubmitElement.click()

