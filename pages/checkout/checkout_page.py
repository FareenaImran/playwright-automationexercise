from pages.base.order_details_base import OrderDetailsBase
from pages.payment.payment_page import PaymentPage


class CheckoutPage(OrderDetailsBase):

    # ___________________________________Locators____________________________________________
    DELIVERY_ADDRESS="#address_delivery"
    BILLING_ADDRESS = "#address_invoice"
    NAME_TEXT=".address_firstname"
    ADDRESS_TEXT=".address_address1"
    STREET_TEXT=".address_address2"
    COUNTRY_TEXT=".address_country_name"
    NUMBER_TEXT=".address_phone"
    CITY_TEXT=".address_city"
    COMMENT_INPUT="textarea[name='message']"
    PLACE_ORDER_BTN="Place Order"


    def __init__(self,page):
        super().__init__(page)
        self.comment_input=self.page.locator(self.COMMENT_INPUT)

    # ___________________________________Methods____________________________________________

    def get_address_details(self,address):
        info=None
        if address.lower()=="billing":  info = self.BILLING_ADDRESS
        elif address.lower=="delivery": info = self.DELIVERY_ADDRESS
        else: raise  ValueError(f"Incorrect value : {address}")
        name_info=self.get_text(self.page.locator(f"{info} {self.NAME_TEXT}"))
        address_info=self.get_text(self.page.locator(f"{info} {self.ADDRESS_TEXT}").nth(2))
        street_info=self.get_text(self.page.locator(f"{info} {self.STREET_TEXT}").nth(1))
        city_info=self.get_text(self.page.locator(f"{info} {self.CITY_TEXT}"))
        country_info=self.get_text(self.page.locator(f"{info} {self.COUNTRY_TEXT}"))
        number_info=self.get_text(self.page.locator(f"{info} {self.NUMBER_TEXT}"))
        return name_info,address_info,street_info,city_info,country_info,number_info

    def verify_address_details(self,first_name,last_name,address,state,city,zip_code,number):
        c_name, c, c_address,c_city_state_zip, c_country,c_number = self.get_address_details("billing")
        # Verify Address Details
        assert (first_name and last_name) in c_name, f"name is not correct"
        assert address in c_address, f"address info is not correct"
        assert (state and city and zip_code) in c_city_state_zip,""
        assert number in c_number, f"number info is not correct"
        return self

    def place_order(self):
        self.add_comment()
        self.click("Place Order",self.PLACE_ORDER_BTN)
        return PaymentPage(self.page)

    def add_comment(self):
        self.comment_input.scroll_into_view_if_needed()
        self.type("Comment",self.comment_input,"This is my comment")
        return self












