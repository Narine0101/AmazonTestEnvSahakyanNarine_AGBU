from pages_.navigationBar import NavigationBar
from pages_.searchResultPage import ResultPage
from pages_.productDetails import ProductDetails
from pages_.cartPage import CartPage
from tests_.baseTest import BaseTestWithoutLogin


class SearchPage(BaseTestWithoutLogin):
    def test_search_product(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_in_search_field("Christmas tree")
        navigationBarObj.click_on_search_button()

        resultPageObj = ResultPage(self.driver)
        resultPageObj.click_on_sort_by_button()
        resultPageObj.click_on_best_sellers_button()
        resultPageObj.click_on_first_product_from_list()

        productDetailsObj = ProductDetails(self.driver)
        cartPageObj = CartPage(self.driver)
        cartPreviousElement = cartPageObj.get_cart_count_element()
        productDetailsObj.click_on_add_to_cart_button()
        cartCurrentElement = cartPageObj.get_cart_count_element()
        self.assertEqual(cartPreviousElement+1, cartCurrentElement)




