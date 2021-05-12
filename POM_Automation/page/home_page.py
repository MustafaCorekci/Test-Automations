from selenium.webdriver.common.by import By
from random import randint
import time


class HomePage:
    """HomePage for go to login page, go to category page"""

    TEST_URL = "https://www.u-buy.co.nz/"
    HOME_PAGE_SELECTOR = (By.XPATH, "//a[@class = 'navbar-brand desktop-hidden']")
    LOGIN_DROPDOWN_BTN = (By.CLASS_NAME, "dropdown-toggle")
    LOGIN_BTN = (By.XPATH, "(//a[@class = 'dropdown-item'])[1]")
    CATEGORY = (By.CSS_SELECTOR, ".img-fluid.p-20")
    CART_PAGE_ICON = (By.CSS_SELECTOR, ".header-cart.pl-3.pr-0")
    VIEW_CART_BTN = (By.CSS_SELECTOR, ".btn.btn-primary.w-80.d-flex")

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def go_to_home_page(self):
        """
        Navigates to home page

        """
        time.sleep(1)
        self.methods.wait_for_element(self.HOME_PAGE_SELECTOR).click()

    def go_to_login_page(self):
        """
        Navigates to login page

        """
        self.methods.hover(self.LOGIN_DROPDOWN_BTN)
        self.methods.execute_script_click(self.LOGIN_BTN)

    def go_to_category_page(self):
        """
        Go to random a category

        """
        time.sleep(1)
        self.methods.wait_for_element(self.CATEGORY)
        random_value = self.driver.find_elements(*self.CATEGORY)
        rand_value = random_value[randint(0, len(random_value) - 1)]
        rand_value.click()
        time.sleep(1)

    def go_to_cart(self):
        """
        Navigates to cart page

        """
        self.methods.execute_script_click(self.CART_PAGE_ICON)
        time.sleep(1)
        self.methods.execute_script_click(self.VIEW_CART_BTN)
