import logging
from pages.home.home_page import HomePage
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestProductReview(BaseTest):
    def test_add_product_review(self,page):
        """Test add product review """
        home=HomePage(page)
        #Add product Review
        alert=(home.goto_products().
               verify_page_heading("All Products").
               view_product(1).add_review("Great Quality!").
               get_alert_msg())
        #Verify alert message
        assert "Thank you" in alert, f"Alert: {alert}"
        log.logger.info(alert)