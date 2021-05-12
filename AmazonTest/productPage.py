from selenium.webdriver.common.by import By

addToList = "add-to-wishlist-button-submit"
viewList = "WLHUC_viewlist"
deleteButton = "(//span/a[@class = 'a-link-normal a-declarative g-visible-js'])[1]"


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def addToListClick(self):
        self.driver.find_element(By.ID, addToList).click()

    def viewListClick(self):
        self.driver.find_element(By.ID, viewList).click()

    def deleteItemClick(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, deleteButton).click()

