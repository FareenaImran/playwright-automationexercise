import logging

import pytest

from pages.home.home_page import HomePage
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
                                 search_product(search_term).verify_searched_product_text().get_product_names())

        #Verify searched term in product names
        success=all(search_term.lower() in name.lower() for name in searched_product_names)
        assert success,f"Failed!! Not all the product names contain '{search_term}'"

        log.logger.info(f"Verified !! All the searched product names contain '{search_term}'")

