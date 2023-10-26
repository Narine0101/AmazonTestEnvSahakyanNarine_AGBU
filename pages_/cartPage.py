from selenium.webdriver.common.by import By


class CartPage():
    def __init__(self, driver):
        self.driver = driver

    def delete_firstProduct_from_cart(self):

        firstProductDeleteButtonElement = self.driver.find_element(By.XPATH, "(//input[@value='Delete'])[1]")

        firstProductDeleteButtonElement.click()




