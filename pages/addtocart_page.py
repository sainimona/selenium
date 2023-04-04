from utlities.locators import *
from base.base_driver import Basedriver


class AddToCart(Basedriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = AddToCartPageLocators

    def add_to_cart(self):
        self.wait_until_element_is_clicklable(*self.locator.CART).click()
        self.wait_until_element_is_clicklable(*self.locator.CHECKOUT).click()

