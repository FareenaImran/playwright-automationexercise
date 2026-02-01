import logging

from pages.base.ae_base_page import AEBasePage
from pages.products.product_details_page import ProductDetailsPage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class ProductsPage(AEBasePage):
    # ___________________________________Locators____________________________________________
    ALL_PRODUCTS_TEXT="All Products"
    PRODUCT=".product-image-wrapper"
    VIEW_PRODUCT="(//a[text()='View Product'])"


    def __init__(self,page):
        super().__init__(page)
        self.product=self.page.locator(self.PRODUCT)


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

