import logging

import pytest

from pages.base.ae_base_page import AEBasePage
from pages.products.product_details_page import ProductDetailsPage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class ProductsPage(AEBasePage):
    # ___________________________________Locators____________________________________________
    ALL_PRODUCTS_TEXT="All Products"
    PRODUCT=".product-image-wrapper"
    VIEW_PRODUCT="(//a[text()='View Product'])"
    SEARCH_INPUT="#search_product"
    SEARCH_BTN="#submit_search"
    SEARCH_PRODUCT_TEXT="Searched Products"
    PRODUCT_NAME=".overlay-content p"


    def __init__(self,page):
        super().__init__(page)
        self.product=self.page.locator(self.PRODUCT)
        self.search_input=self.page.locator(self.SEARCH_INPUT)
        self.product_names=self.page.locator(self.PRODUCT_NAME)


    # ___________________________________Methods____________________________________________

    def verify_product_page(self):
        self.verify_page_heading(self.ALL_PRODUCTS_TEXT)
        return self

    def verify_product_list(self):
        self.is_visible("Product List",self.product.first)
        return self

    def view_product(self,product_card_no):
        self.click("View Product",f"{self.VIEW_PRODUCT}[{product_card_no}]")
        return ProductDetailsPage(self.page)

    def search_product(self,text):
        self.type("Search Text",self.search_input,text)
        self.click("Search Icon",self.SEARCH_BTN)
        return self

    def verify_searched_product_text(self):
        self.verify_page_heading(self.SEARCH_PRODUCT_TEXT)
        return self

    def get_product_names(self):
        product_names=self.get_text(self.product_names,True)
        if not product_names:
            pytest.skip("No Records Found...")
        return product_names


