from utlities.locators import *
from base.base_driver import Basedriver


class Product(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = ProductPageLocators

    def select_product(self):
        self.wait_until_element_is_clicklable(*self.locator.PRODUCT).click()
