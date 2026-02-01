import logging

from pages.base.ae_base_page import AEBasePage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class ProductDetailsPage(AEBasePage):
    # ___________________________________Locators____________________________________________
    PRODUCT_DETAIL_URL="product_details"
    PRODUCT_INFO=".product-information"
    PRODUCT_NAME=".product-information h2"
    PRODUCT_CATEGORY="p:has-text('Category')"
    PRODUCT_PRICE="span:has-text('Rs.')"
    PRODUCT_AVAILABILITY="p:has-text('Availability')"
    PRODUCT_CONDITION="p:has-text('Condition')"
    PRODUCT_BRAND="p:has-text('Brand')"


    def __init__(self,page):
        super().__init__(page)
        self.product_info=self.page.locator(self.PRODUCT_INFO)
        self.product_name=self.page.locator(self.PRODUCT_NAME)
        self.product_category=self.page.locator(self.PRODUCT_CATEGORY)
        self.product_price=self.page.locator(self.PRODUCT_PRICE).nth(1)
        self.product_availability=self.page.locator(self.PRODUCT_AVAILABILITY)
        self.product_condition=self.page.locator(self.PRODUCT_CONDITION)
        self.product_brand=self.page.locator(self.PRODUCT_BRAND)

    # ___________________________________Methods____________________________________________

    def verify_product_details_url(self):
        self.verify_url(self.PRODUCT_DETAIL_URL)
        return self

    def verify_product_details(self):
        self.is_visible("Product Info", self.product_info)
        self.verify_product_name()
        self.verify_product_category()
        self.verify_product_price()
        self.verify_product_availability()
        self.verify_product_condition()
        self.verify_product_brand()
        return self

    def verify_product_name(self):
        text=self.get_text(self.product_name)
        self.is_visible(text,self.product_name)
        return self

    def verify_product_category(self):
        text = self.get_text(self.product_category)
        self.is_visible(text, self.product_category)
        return self

    def verify_product_price(self):
        text = self.get_text(self.product_price)
        self.is_visible(text, self.product_price)
        return self

    def verify_product_availability(self):
        text = self.get_text(self.product_availability)
        self.is_visible(text, self.product_availability)
        return self

    def verify_product_condition(self):
        text = self.get_text(self.product_condition)
        self.is_visible(text, self.product_condition)
        return self

    def verify_product_brand(self):
        text = self.get_text(self.product_brand)
        self.is_visible(text, self.product_brand)
        return self
