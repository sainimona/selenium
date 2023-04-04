from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.ID, 'login-button')
    PATH = "/Users/monasaini/PycharmProjects/TestFrameworkDemo/pages/screenshots"
    RES = PATH + "failure.png"


class ProductPageLocators(object):
    PRODUCT = (By.ID, 'add-to-cart-sauce-labs-backpack')


class AddToCartPageLocators(object):
    CART = (By.ID, 'shopping_cart_container')
    CHECKOUT = (By.ID, 'checkout')


class InformationPageLocators(object):
    FIRSTNAME = (By.ID, 'first-name')
    LASTNAME = (By.ID, 'last-name')
    ZIPCODE = (By.ID, 'postal-code')
    CONTINUE = (By.ID, 'continue')


class FinishPageLocators(object):
    FINISH = (By.ID, 'finish')
    ACTUAL = (By.CSS_SELECTOR, "h2.complete-header")
