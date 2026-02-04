import logging

from pages.base.ae_base_page import AEBasePage
from pages.products.view_cart_page import ViewCartPage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class ProductBasePage(AEBasePage):
    VIEW_CART="View Cart"
    CONT_SHOP_BTN="Continue Shopping"
    ADD_TO_CART_BTN="Add to cart"



    def __init__(self,page):
        super().__init__(page)

    def view_cart(self):
        self.click("View Cart",self.VIEW_CART)
        return ViewCartPage(self.page)

    def continue_shopping(self):
        self.click("Continue Shopping", self.CONT_SHOP_BTN)
        return self

    def add_to_cart(self):
        self.click("Add to cart",self.ADD_TO_CART_BTN)
        return self