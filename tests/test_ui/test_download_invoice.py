import logging
from pages.base.order_details_base import OrderDetailsBase
from pages.checkout.checkout_page import CheckoutPage
from pages.products.products_page import ProductsPage
from pages.products.view_cart_page import ViewCartPage
from pages.home.home_page import HomePage
from pages.signup.signup_base import SignupBase
from tests.base_test import BaseTest
from utils.helpers.auth_helper import signup, delete_user
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestDownloadInvoice(BaseTest):

    def test_download_invoice_after_purchase_order(self,page):
        """Download invoice after purchase order"""
        #Get User Data
        data=SignupBase(page)
        first_name,last_name,address,state,city,zip_code,number=data.get_address_data()

        #Navigate to products page
        home=HomePage(page)
        home.verify_home_page().goto_products()

        #Get Product Name
        product=ProductsPage(page)
        product_name=product.get_product_name(1)
        #Add to cart product
        product.add_to_cart(1).view_cart()

        #View cart
        cart=ViewCartPage(page)
        cart.verify_view_cart_page().proceed_to_checkout().signup_or_login()

        #Signup
        username,_,_=signup(page)
        #Login Username
        home.verify_logged_in_username(username).goto_cart().proceed_to_checkout()

        # Get all product description from cart table
        info=OrderDetailsBase(page)
        descriptions=info.get_all_products_desc()
        #Verify Product Names
        assert any(product_name in desc for desc in descriptions),f"{product_name} does not match with {descriptions}"

        # Verify address details
        checkout = CheckoutPage(page)
        download_info=(checkout.
         verify_address_details(first_name,last_name,address,city,state,zip_code,number).
         place_order().
         enter_payment_details("Fareena","09000000098000","909",'02',"2030").
         pay_and_confirm_order().verify_confirm_order_msg().download_invoice())

        #Verify download
        assert download_info.suggested_filename=="invoice.txt",f"Downloaded File name :{download_info.suggested_filename}"

        log.logger.info("Verified! File downloaded successfully")

        #Delete Account
        delete_user(page)







