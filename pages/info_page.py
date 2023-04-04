from utlities.locators import *
from base.base_driver import Basedriver


class Information(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = InformationPageLocators

    def info_details(self, firstname, lastname, pin):
        self.wait_until_element_is_located(*self.locator.FIRSTNAME).send_keys(firstname)
        self.wait_until_element_is_located(*self.locator.LASTNAME).send_keys(lastname)
        self.wait_until_element_is_located(*self.locator.ZIPCODE).send_keys(pin)

    def click_continue_button(self):
        self.wait_until_element_is_clicklable(*self.locator.CONTINUE).click()
