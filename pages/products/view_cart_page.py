import logging

from pages.base.order_details_base import OrderDetailsBase
from pages.signup.signup_login_page import SignupLoginPage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class ViewCartPage(OrderDetailsBase):

    # ___________________________________Locators____________________________________________
    ROWS="//tbody//tr"
    PRODUCT_DATA="#product-"
    PROCEED_TO_CHECKOUT_BTN="Proceed To Checkout"
    REG_LOGIN_TEXT="Register / Login"

    def __init__(self, page):
        super().__init__(page)
        self.rows=self.page.locator(self.ROWS)

    # ___________________________________Methods____________________________________________

    def verify_view_cart_page(self):
        self.verify_page("Cart",True)
        return self

    def get_rows(self):
        total=self.rows.count()
        return total

    def proceed_to_checkout(self):
        self.click("Proceed To Checkout",self.PROCEED_TO_CHECKOUT_BTN)
        return self

    def signup_or_login(self):
        self.click("Register / Login",self.REG_LOGIN_TEXT)
        return SignupLoginPage(self.page)

    # def get_all_products_desc(self):
    #     return self.get_text(self.prod_desc,True)
    #
    # def get_all_products_price(self):
    #     prices_text= self.get_text(self.prod_price,True)
    #     all_prices=[re.search(r'\d+',price).group() for price in prices_text]
    #     return all_prices
    #
    # def get_all_products_quantity(self):
    #     return self.get_text(self.prod_quan, True)
    #
    # def get_all_products_total(self):
    #     total_texts=self.get_text(self.prod_total, True)
    #     total_list=[re.search(r'\d+',total).group() for total in total_texts]
    #     return total_list






