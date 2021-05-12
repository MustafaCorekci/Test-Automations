from selenium.webdriver.common.by import By
import time


class ProductPage:
    """Product page to select size and add to cart."""

    ADD_TO_CART_BTN = (By.ID, "add-to-cart-btn")
    OUT_OF_STOCK = (By.CLASS_NAME, "out-of-stock")
    CONTINUE_SHOPPING = (By.CLASS_NAME, "continue-shipping")

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def product_page_load_and_stock_info(self):
        """
        Product stock control

        """
        stock_info = self.methods.element_exists(self.OUT_OF_STOCK)
        add_to_cart_button = self.methods.element_exists(self.ADD_TO_CART_BTN)
        if stock_info or not add_to_cart_button:
            return True
        else:
            return False

    def add_to_cart(self):
        """
        Adds product to the cart page

        """
        self.methods.wait_for_element(self.ADD_TO_CART_BTN).click()
        time.sleep(1)
        self.methods.execute_script_click(self.CONTINUE_SHOPPING)
        time.sleep(1)
