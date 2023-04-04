from utlities.locators import *
from base.base_driver import Basedriver


class Finish(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = FinishPageLocators

    def finish_payment(self):
        self.wait_until_element_is_clicklable(*self.locator.FINISH).click()

    def verify_success_msg(self):
        msg = self.wait_until_element_is_located(*self.locator.ACTUAL).text
        if msg == "Thank you for your order!":
            assert True
        else:
            assert False