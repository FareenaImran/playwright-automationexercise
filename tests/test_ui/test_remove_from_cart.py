import logging

from pages.home.home_page import HomePage
from pages.products.products_page import ProductsPage
from pages.products.view_cart_page import ViewCartPage
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestAddToCart(BaseTest):

    def test_remove_product_from_cart(self,page):
        """Verify clicking on 'X' icon removes product from cart table"""

        home = HomePage(page)
        home.goto_products()

        # Add to cart
        product = ProductsPage(page)
        product.add_to_cart(1).continue_shopping().add_to_cart(2).view_cart()

        # Verify rows in table
        view_cart = ViewCartPage(page)

        #1st product description
        first_product_desc=view_cart.get_row_description(1)

        #remove 1st product from tabel
        view_cart.remove_product(1)

        # Get all products description from table
        descriptions = view_cart.get_all_products_desc()

       # Verify name
        assert first_product_desc not in descriptions,f"Product '{first_product_desc}' has not removed from table records :'{descriptions}'"

        log.logger.info(f"Verified!! Item removed successfullly")

