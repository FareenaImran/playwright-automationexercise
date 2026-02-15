import logging
from pages.home.home_page import HomePage
from pages.home.recommended_section_page import RecommendedSectionPage
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestRecommendedSection(BaseTest):
    def test_add_recommended_product_in_cart(self,page):
        """Test add recommended product in cart"""
        home=HomePage(page)
        # Get recommended product name
        product_name=home.goto_recommended_products().get_product_name(1)
        # Add to cart recommended product and Get cart products' descriptions
        recommended_product=RecommendedSectionPage(page)
        product_desc=recommended_product.add_to_cart(1).view_cart().get_all_products_desc()
        # Verify product name in cart
        assert any(product_name in desc for desc in product_desc),f"Product name '{product_name}' doesn't exists in {product_desc}"
        log.logger.info(f"Verified ! Recommended Product '{product_name}'added in cart")