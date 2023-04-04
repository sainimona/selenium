import pytest
from pages.login_page import Login
from pages.product_page import Product
from pages.addtocart_page import AddToCart
from pages.info_page import Information
from pages.finish_page import Finish


@pytest.mark.usefixtures("setup")
class TestShoppingAndVerifyPayment:
    def test_add_to_cart(self):
        login = Login(self.driver)
        login.enter_credentials("standard_user", "secret_sauce123")
        login.click_login_button()
        product = Product(self.driver)
        product.select_product()
        cart = AddToCart(self.driver)
        cart.add_to_cart()
        info = Information(self.driver)
        info.info_details("Mona", "Saini", "123456")
        info.click_continue_button()
        finish = Finish(self.driver)
        finish.finish_payment()
        finish.verify_success_msg()
