import logging
import re
import pytest
from pages.products.product_base_page import ProductBasePage
from pages.products.product_details_page import ProductDetailsPage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class ProductsPage(ProductBasePage):
    # ___________________________________Locators____________________________________________
    ALL_PRODUCTS_TEXT="All Products"
    PRODUCT="//*[contains(@class,'product-image-wrapper')]"
    VIEW_PRODUCT="//a[text()='View Product']"
    SEARCH_INPUT="#search_product"
    SEARCH_BTN="#submit_search"
    SEARCH_PRODUCT_TEXT="Searched Products"
    PRODUCT_NAME="//*[contains(@class,'overlay-content')]//p"
    PRODUCT_PRICE=".product-overlay h2"
    ADD_TO_CART_BTN="//*[contains(@class,'product-overlay')]//a[text()='Add to cart']"



    def __init__(self,page):
        super().__init__(page)
        self.product=self.page.locator(self.PRODUCT)
        self.search_input=self.page.locator(self.SEARCH_INPUT)
        self.product=self.page.locator(self.PRODUCT)
        self.product_price = self.page.locator(self.PRODUCT_PRICE)


    # ___________________________________Methods____________________________________________

    def verify_product_page(self,heading_name):
        self.verify_page_heading(heading_name)
        return self

    def verify_product_list(self):
        self.is_visible("Product List",self.product.first)
        return self

    def view_product(self,product_card_no):
        self.click("View Product",f"({self.VIEW_PRODUCT})[{product_card_no}]")
        return ProductDetailsPage(self.page)

    def search_product(self,text):
        self.type("Search Text",self.search_input,text)
        self.click("Search Icon",self.SEARCH_BTN)
        return self

    def verify_searched_product_text(self):
        self.verify_page_heading(self.SEARCH_PRODUCT_TEXT)
        return self

    def get_all_product_names(self):
        product_names=self.get_text(self.product_name,True)
        if not product_names: pytest.skip("No Records Found...")
        return product_names

    def get_product_details(self,index_no):
        name=self.get_product_name(index_no)
        price=self.get_product_price(index_no)
        return name,price

    def add_to_cart(self,index_no:int):
        product=f"({self.PRODUCT})[{index_no}]"
        self.hover(product)
        add_to_cart_btn=f"({self.ADD_TO_CART_BTN})[{index_no}]"
        self.click("Add To Cart", add_to_cart_btn)
        return self
    
    def get_product_name(self,index_no):
        product_name=f"({self.PRODUCT_NAME})[{index_no}]"
        return self.get_text(self.page.locator(product_name))

    def get_product_price(self,index_no):
        product_price=self.product_price.nth(index_no)
        prices_text=self.get_text(product_price)
        price_count=re.search(r'\d+',prices_text).group()
        return price_count


