from selenium.webdriver.common.by import By


class LoginPage:
    """Website login page to user logged in."""

    MAIL = "mail"
    PASSWORD = "password"
    USERNAME_TEXT_BOX = (By.ID, "login.username")
    PASSWORD_TEXT_BOX = (By.ID, "login.password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.mt-4.w-60")

    def __init__(self, driver, methods):
        self.driver = driver
        self.methods = methods

    def login(self):
        """
        Fills login information

        """
        self.methods.wait_for_element(self.USERNAME_TEXT_BOX).send_keys(self.MAIL)
        self.methods.wait_for_element(self.PASSWORD_TEXT_BOX).send_keys(self.PASSWORD)
        self.methods.wait_for_element(self.SIGN_IN_BUTTON).click()
