from selenium.webdriver.common.by import By

loginOpenButton = "nav-link-accountList"
emailTextbox = "ap_email"
passwordTextbox = "ap_password"
loginEmailButton = "continue"
loginPasswordButton = "signInSubmit"


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def openLoginPage(self):
        self.driver.find_element(By.ID, loginOpenButton).click()

    def enterMail(self, email):
        self.driver.find_element(By.ID, emailTextbox).send_keys(email)

    def clickEmailLogin(self):
        self.driver.find_element(By.ID, loginEmailButton).click()

    def enterPassword(self, password):
        self.driver.find_element(By.ID, passwordTextbox).send_keys(password)

    def clickPasswordLogin(self):
        self.driver.find_element(By.ID, loginPasswordButton).click()
