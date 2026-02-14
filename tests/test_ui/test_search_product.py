import logging
from pages.home.home_page import HomePage
from pages.products.products_page import ProductsPage
from pages.signup.signup_base import SignupBase
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestProducts(BaseTest):
    def test_search_product(self,page,keyword):
        """
        Test that user get the correct product list on search
        :parameter: blue , hello
        """
        search_term=keyword

        #Search Product
        home=HomePage(page)
        searched_product_names=(home.verify_home_page().goto_products().verify_product_page("All Products").
                                 search_product(search_term).verify_searched_product_text().get_all_product_names())

        #Verify searched term in product names
        success=all(search_term.lower() in name.lower() for name in searched_product_names)
        assert success,f"Failed!! Not all the product names contain '{search_term}'"

        log.logger.info(f"Verified !! All the searched product names contain '{search_term}'")

    def test_search_product_and_verify_login_cart(self,page):
        search_term = "blue"

        # Search Product and get all searched products names
        home = HomePage(page)
        searched_product_names = (home.
                                  verify_home_page().
                                  goto_products().
                                  verify_product_page("All Products").
                                  search_product(search_term).
                                  verify_searched_product_text().
                                  get_all_product_names())

        # Verify searched term in product names
        success = all(search_term.lower() in name.lower() for name in searched_product_names)
        assert success, f"Failed!! Not all the product names contain '{search_term}'"

        log.logger.info(f"Total Searched Products:{len(searched_product_names)}")

        # Add all searched products to cart
        product = ProductsPage(page)
        for i in range(1,len(searched_product_names)+1):
            product.add_to_cart(i).continue_shopping()

        # Verify add to cart products in cart table
        all_product_desc=home.goto_cart().get_all_products_desc()
        assert all(
            any(product in desc for desc in all_product_desc)
            for product in searched_product_names
        ), f"Not all products found in cart: {all_product_desc}"

        # Login
        data=SignupBase(page)
        _,email,password=data.get_login_cred()
        home.go_to_signup_or_login().login(email,password)
        home.goto_cart()

        # Again Verify add to cart products in cart table
        all_product_desc = home.goto_cart().get_all_products_desc()

        assert all(
            any(product in desc for desc in all_product_desc)
            for product in searched_product_names
        ), f"Not all products found in cart: {all_product_desc}"

        log.logger.info("Verified! Add to cart shows correct details after login")
