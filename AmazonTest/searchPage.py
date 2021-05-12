from selenium.webdriver.common.by import By
import time

searchTextbox = "twotabsearchtextbox"
searchButton = "//input[@class = 'nav-input' and @value = 'Go'] "
secondPageButton = "//li[@class = 'a-normal']//a[text() = '2']"
productPage = "(//h2[@class = 'a-size-mini a-spacing-none a-color-base s-line-clamp-2']//a)[3]"


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def enterSearchText(self, text):
        self.driver.find_element(By.ID, searchTextbox).send_keys(text)
        assert (self.driver.find_element(By.ID, searchTextbox)).get_attribute("value") == text,\
            "Aynı Değil ! ! !"

    def clickSearch(self):
        self.driver.find_element(By.XPATH, searchButton).click()

    def clickSecondPage(self):
        self.driver.find_element(By.XPATH, secondPageButton).click()

    def productClick(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, productPage).click()
