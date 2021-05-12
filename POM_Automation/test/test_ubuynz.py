from happy_path_ubuynz.test.setup_ubuynz import Setup
from base.base_test import *
import unittest


@Owner.mustafa_corekci
@Priority.LOW
@decorator_loader(error_logger)
class UbuynzHappyPath(BaseTest):
    """ Test case is:

      1. Go to given website
      2. Click login page button
      3. Try to logged in
      4. Go to random category page
      5. Select one random product
      6. Select product size
      7. Add product to cart
      8. Go to cart page
      9. Go to checkout page if isUserLoggedIn rule returns true
      10. Delete all items from cart and tear down

    """
    def setUp(self):
        Setup.__init__(self)

    def test_ubuynz(self):
        self.home_page_ubuynz.go_to_login_page()
        self.login_page_ubuynz.login()
        self.home_page_ubuynz.go_to_home_page()
        self.home_page_ubuynz.go_to_category_page()
        self.category_page_ubuynz.click_random_product()
        while self.product_page_ubuynz.product_page_load_and_stock_info():
            self.home_page_ubuynz.go_to_home_page()
            self.home_page_ubuynz.go_to_category_page()
            self.category_page_ubuynz.click_random_product()
        self.product_page_ubuynz.add_to_cart()
        self.home_page_ubuynz.go_to_cart()
        self.cart_page_ubuynz.go_to_checkout()
        self.cart_page_ubuynz.back_to_cart()
        self.cart_page_ubuynz.remove_items_from_cart()
        self.assertTrue(self.cart_page_ubuynz.is_empty_cart_present(),
                        'No "Cart is not empty!')

    def tearDown(self):
        self.quit_driver()


if __name__ == '__main__':
    unittest.main()
