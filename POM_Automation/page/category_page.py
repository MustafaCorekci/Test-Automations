from selenium.webdriver.common.by import By
import random
import time


class CategoryPage:
    """CategoryPage is selecting one random product from category page."""

    PRODUCT = (By.XPATH, "//div[@class = 'product-image']//a")

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def click_random_product(self):
        """
        Navigate to random product

        """
        self.methods.wait_for_element(self.PRODUCT)
        product_list = self.driver.find_elements(*self.PRODUCT)
        product = product_list[random.randint(0, len(product_list) - 1)]
        product.click()
        time.sleep(2)
