from utlities.locators import *
from base.base_driver import Basedriver


class Login(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = LoginPageLocators

    def enter_credentials(self, uname, password):
        self.wait_until_element_is_located(*self.locator.USERNAME).send_keys(uname)
        self.wait_until_element_is_located(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.wait_until_element_is_clicklable(*self.locator.SUBMIT).click()
