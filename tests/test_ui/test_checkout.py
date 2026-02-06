import logging

from pages.base.order_details_base import OrderDetailsBase
from pages.checkout.checkout_page import CheckoutPage
from pages.products.product_base_page import ProductBasePage
from pages.products.products_page import ProductsPage
from pages.products.view_cart_page import ViewCartPage
from pages.home.home_page import HomePage
from pages.signup.signup_base import SignupBase
from tests.base_test import BaseTest
from utils.helpers.auth_helper import signup, delete_user
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestCheckout(BaseTest):

    def test_place_order_with_signup(self,page):
        """Place Order: Register While Checkout"""
        #Get User Data
        data=SignupBase(page)
        first_name,last_name,address,state,city,zip_code,number=data.get_address_data()

        add_product=2
        add_to_cart=[]

        #Navigate to products page
        home=HomePage(page)
        home.verify_home_page().goto_products()

        #Add to cart the view cart
        product=ProductsPage(page)
        for i in range(add_product):
          #Get Product Name
          product_name=product.get_product_name(i)
          add_to_cart.append(product_name)

          product.add_to_cart(i+1).continue_shopping()
          if i==add_product-1: product.add_to_cart(i+1).view_cart()

        #View cart
        cart=ViewCartPage(page)
        cart.verify_view_cart_page().proceed_to_checkout().signup_or_login()

        #Signup
        username,_,_=signup(page)
        #Login Username
        home.verify_logged_in_username(username).goto_cart().proceed_to_checkout()

        #Verify Product Names
        info=OrderDetailsBase(page)
        descriptions=info.get_all_products_desc()
        assert all(any(product in desc for desc in descriptions) for product in add_to_cart), \
            f"{add_to_cart} does not match with {descriptions}"

        # Verify address details
        checkout = CheckoutPage(page)
        (checkout.
         verify_address_details(first_name,last_name,address,city,state,zip_code,number).
         place_order().
         enter_payment_details("Fareena","09000000098000","909",'02',"2030").
         pay_and_confirm_order().verify_confirm_order_msg())

        #Delete Account
        delete_user(page)







