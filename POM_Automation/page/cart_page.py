from selenium.webdriver.common.by import By


class CartPage:
    """CartPage is making cart empty."""

    GO_TO_CHECKOUT = (By.CLASS_NAME, "overview-btn")
    BACK_TO_CART_ICON = (By.ID, "item_qty")
    REMOVE_ITEM = (By.XPATH, "//a[@class = 'action']")
    EMPTY_CART = (By.CLASS_NAME, "empty-cart-page")

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def go_to_checkout(self):
        """
        Navigates the checkout page

        """
        self.methods.wait_for_element(self.GO_TO_CHECKOUT).click()

    def back_to_cart(self):
        """
        Navigates the come back to the cart page

        """
        self.methods.wait_for_element(self.BACK_TO_CART_ICON).click()

    def is_empty_cart_present(self):
        """
        Check if there is any product left on the cart page

        """
        return self.methods.is_element_present(self.EMPTY_CART)

    def remove_items_from_cart(self):
        """
        Deletes products from the cart page

        """
        self.methods.wait_for_element(self.REMOVE_ITEM).click()
