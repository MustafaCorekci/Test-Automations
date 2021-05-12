import random
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def wait_for_element(self, selector):
        """
        Wait for element to present
        :param str selector: locator of the element to find

        """
        try:
            return self.wait.until(ec.element_to_be_clickable(selector))
        except TimeoutException:
            return self.wait.until(ec.presence_of_element_located(selector))

    def wait_till_element_disappears(self, selector):
        """
        Wait for element to disappears
        :param str selector: locator of the element to find

        """
        return self.wait.until(ec.invisibility_of_element_located(selector))

    def switch_tab(self, tab_index):
        """
        Switch tab from the current tab
        :param int tab_index: index numbers of the selecting tab

        """
        self.driver.switch_to_window(self.driver.window_handles[tab_index])

    def hover(self, selector):
        """
        Hover over the selected element
        :param str selector: locator of the element to find

        """
        hover_element = self.wait_for_element(selector)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()

    def random_number(first_value, second_value):
        """
        Return random number between parameters
        :param int first_value: begining value of the range
        :param int second_value: last value of the range

        """
        return random.randint(first_value, second_value)

    def element_exists(self, selector):
        """
        Return true if element present and false if element absent
        :param str selector: locator of the element to find

        """
        try:
            self.wait.until(ec.presence_of_element_located(selector))
            return True
        except TimeoutException:
            return False

    def set_cookie(self, name, value):
        """
        Sets a cookie in given variables
        :param str name: name of the cookie
        :param str value: value of the given cookie name

        """
        cookie = {'name': name, 'value': value, 'path': '/'}
        self.driver.add_cookie(cookie)

    def execute_script_click(self, selector):
        """
        Try click from script code
        :param str selector: locator of the element to click

        """
        try:
            self.wait_for_element(selector).click()
        except ElementClickInterceptedException or ElementNotInteractableException or TimeoutException:
            element = self.wait_for_element(selector)
            self.driver.execute_script("""
                    arguments[0].click();
                    """, element)

    def is_element_present(self, locator):
        """
        Return True if element present and False if element absent
        :param locator: locator of the element to find
        """
        try:
            self.driver.find_element(*locator)
        except (NoSuchElementException, StaleElementReferenceException):
            return False
        return True
