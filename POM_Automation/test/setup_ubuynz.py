from happy_path_ubuynz.page.home_page import HomePage
from happy_path_ubuynz.page.category_page import CategoryPage
from happy_path_ubuynz.page.cart_page import CartPage
from happy_path_ubuynz.page.login_page import LoginPage
from happy_path_ubuynz.page.product_page import ProductPage
from happy_path_ubuynz.base.page_base import BaseClass
from selenium import webdriver


class Setup:
    def __init__(self):
        TEST_URL = 'https://www.u-buy.co.nz/'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.methods = BaseClass(self.driver)
        self.home_page_ubuynz = HomePage(self.driver, self.methods)
        self.login_page_ubuynz = LoginPage(self.driver, self.methods)
        self.category_page_ubuynz = CategoryPage(self.driver, self.methods)
        self.product_page_ubuynz = ProductPage(self.driver, self.methods)
        self.cart_page_ubuynz = CartPage(self.driver, self.methods)
        self.driver.get(TEST_URL)
