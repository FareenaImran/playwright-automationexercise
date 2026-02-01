import logging
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

