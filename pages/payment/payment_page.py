import logging

from pages.base.ae_base_page import AEBasePage
from pages.place_order.place_order_page import PlaceOrderPage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)
class PaymentPage(AEBasePage):

    # ___________________________________Locators____________________________________________

    NAME_ON_CARD_INPUT='[data-qa="name-on-card"]'
    CARD_NUM_INPUT='[data-qa="card-number"]'
    CVC_INPUT='[data-qa="cvc"]'
    EXPIRE_MM_INPUT='[data-qa="expiry-month"]'
    EXPIRE_YYYY_INPUT='[data-qa="expiry-year"]'
    CONFIRM_BTN="#submit"
    SUCCESS_MSG="#success_message"


    def __init__(self,page):
        super().__init__(page)
        self.name_on_card_input=self.page.locator(self.NAME_ON_CARD_INPUT)
        self.card_num_input=self.page.locator(self.CARD_NUM_INPUT)
        self.cvc_input=self.page.locator(self.CVC_INPUT)
        self.expire_month_input=self.page.locator(self.EXPIRE_MM_INPUT)
        self.expire_year_input=self.page.locator(self.EXPIRE_YYYY_INPUT)
        self.success_msg=self.page.locator(self.SUCCESS_MSG)

    # ___________________________________Methods____________________________________________

    def enter_payment_details(self,name,card_num,cvc,month,year):
        self.type("Name on card",self.name_on_card_input,name)
        self.type("Card Number",self.card_num_input,card_num,True)
        self.type("CVC",self.cvc_input,cvc,True)
        self.type("Expiration Month",self.expire_month_input,month)
        self.type("Expiration Year",self.expire_year_input,year)
        return self

    def pay_and_confirm_order(self):
        self.click("Pay and Confirm Order",self.CONFIRM_BTN)
        return PlaceOrderPage(self.page)

    def verify_confirm_order_msg(self):
        msg=self.get_text(self.success_msg)
        assert "placed" in msg, f"Error: {msg}"
        return self





