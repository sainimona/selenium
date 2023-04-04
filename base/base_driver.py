import sys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from utlities.locators import *

gir
class Basedriver():
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocators

    def wait_until_element_is_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.presence_of_element_located((locator_type, locator)))
            return element

        except TimeoutException as err:
            self.driver.save_screenshot(*self.locator.RES)
            self.driver.close()
            sys.exit()

    def wait_until_element_is_clicklable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
            return element
        except:
            self.driver.save_screenshot(*self.locator.RES)
            self.driver.close()
            sys.exit()
