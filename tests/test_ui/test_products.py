import logging
import pytest
from pages.home.home_page import HomePage
from pages.products.product_base_page import ProductBasePage
from pages.products.product_details_page import ProductDetailsPage
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestProducts(BaseTest):

    def test_product_details(self,page):
        """
        Test that product details are visible
        """
        home=HomePage(page)
        (home.verify_home_page().
         goto_products().
         verify_product_page().
         verify_product_list().
         view_product(1).
         verify_product_details_url().
         verify_product_details())

        log.logger.info("Verified !!Product Details are Visible")

    @pytest.mark.parametrize("keyword",["blue","hello"])
    def test_search_product(self,page,keyword):
        """
        Test that user get the correct product list on search
        :parameter: blue , hello
        """
        search_term=keyword

        #Search Product
        home=HomePage(page)
        searched_product_names=(home.verify_home_page().goto_products().verify_product_page().
                                 search_product(search_term).verify_searched_product_text().get_all_product_names())

        #Verify searched term in product names
        success=all(search_term.lower() in name.lower() for name in searched_product_names)
        assert success,f"Failed!! Not all the product names contain '{search_term}'"

        log.logger.info(f"Verified !! All the searched product names contain '{search_term}'")

    def test_product_quantity_in_view_cart(self,page):
        """
        Test that quantity updates in view cart when user add from product detail page
        """
        #Navigate to product detail page
        home=HomePage(page)
        home.verify_home_page().goto_products().view_product(1)

        #Get added quantity
        detail =ProductDetailsPage(page)
        quantity_detail=detail.increase_or_decrease_quan("add",3).get_product_quantity()
        log.logger.info(f"Added Quantity: {quantity_detail}")

        #Get Quantity from Table
        cart=ProductBasePage(page)
        view_cart_quantity=cart.click_add_to_cart().view_cart().get_all_products_quantity()
        log.logger.info(f"Quantity In Table: {quantity_detail}")

        #Verify Quantity
        assert quantity_detail in view_cart_quantity,\
            f"Expected {quantity_detail} but got {view_cart_quantity}"

        log.logger.info("Verified!! View Cart quantity shows correct data")
