import logging
from asyncio import timeout_at

from pages.base.order_details_base import OrderDetailsBase
from pages.signup.signup_login_page import SignupLoginPage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class ViewCartPage(OrderDetailsBase):

    # ___________________________________Locators____________________________________________
    TABLE_ROW="//tbody//tr"
    PRODUCT_DATA="#product-"
    PROCEED_TO_CHECKOUT_BTN="Proceed To Checkout"
    REG_LOGIN_TEXT="Register / Login"
    REMOVE_ICON="//*[@class='cart_quantity_delete']"

    def __init__(self, page):
        super().__init__(page)
        self.row=self.page.locator(self.TABLE_ROW)

    # ___________________________________Methods____________________________________________

    def verify_view_cart_page(self):
        self.verify_page("Cart",True)
        return self

    def get_rows(self):
        total=self.row.count()
        return total

    def proceed_to_checkout(self):
        self.click("Proceed To Checkout",self.PROCEED_TO_CHECKOUT_BTN)
        return self

    def signup_or_login(self):
        self.click("Register / Login",self.REG_LOGIN_TEXT)
        return SignupLoginPage(self.page)

    def remove_product(self,index):
        row_item=f"({self.REMOVE_ICON})[{index}]"
        self.click("Remove Icon",row_item)
        self.page.reload()
        return self






