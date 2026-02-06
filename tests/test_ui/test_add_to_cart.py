import logging
from pages.home.home_page import HomePage
from pages.products.products_page import ProductsPage
from pages.products.view_cart_page import ViewCartPage
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestAddToCart(BaseTest):

    def test_add_to_cart_shows_correct_details_in_table(self,page):
        """
        Test that add to cart display correct product's details in table
        """
        products_detail=[]

        home=HomePage(page)
        home.goto_products()

        product=ProductsPage(page)
        #Get Product Details
        for number in range(2):
             product_info = {}
             name,price=product.get_product_details(number)
             product_info["name"],product_info["price"]=name,price
             products_detail.append(product_info)

        #Add to cart
        product.add_to_cart(1).continue_shopping().add_to_cart(2).view_cart()

        #Verify rows in table
        view_cart=ViewCartPage(page)
        assert view_cart.get_rows()==2,f"There should be only 2 products in the table"

        #Verify Name and Price
        descriptions=view_cart.get_all_products_desc()
        prices=view_cart.get_all_products_price()

        for product in products_detail:
            #Verify name
            assert any(product["name"] in desc for desc in descriptions),\
            f"Product Name '{product['name']}' not found in '{descriptions}'"
            #Verify price
            assert any(product["price"] in price for price in prices), \
                f"Product Price '{product['price']}' not found in '{prices}'"

        log.logger.info(f"Verified!! Product details are Correct in table")

    def test_total_count_in_view_cart_table(self,page):
        """Test that total count in view cart is correct"""

        #Add to cart
        home=HomePage(page)
        (home.goto_products().add_to_cart(1).continue_shopping().
         add_to_cart(2).continue_shopping().
         add_to_cart(2).view_cart())

        #Get all Prices , Quantities and Totals from View Cart Table
        view_cart=ViewCartPage(page)
        prices=[int(amount) for amount in view_cart.get_all_products_price()]
        quantities=[int(quan) for quan in view_cart.get_all_products_quantity()]
        total_list=[int(total) for total in view_cart.get_all_products_total()]

        #Verify Total Count
        for i in range(len(prices)):
            total=prices[i]*quantities[i]
            assert total==total_list[i],f"Error: {total} != {total_list[i]}"
            log.logger.info(f"Product{i + 1} : {prices[i]}*{quantities[i]}={total}")

        log.logger.info(f"Verified! Total Counts are correct in view cart table")

