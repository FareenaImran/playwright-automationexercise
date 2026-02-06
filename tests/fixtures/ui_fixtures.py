# import logging
#
# import pytest
# from pages.home.home_page import HomePage
# from pages.signup.signup_base import SignupBase
# from utils.log_util import Logger
#
# log=Logger(__name__,logging.INFO)
#
# @pytest.fixture
# def signup(page):
#     #Get Signup Email and Username
#     cred=SignupBase(page)
#     username,email=cred.get_signup_data()
#     #SignUp
#     home = HomePage(page)
#     (home.verify_home_page().go_to_signup_or_login().verify_signup_page().signup_user(username,email).
#      enter_account_info().enter_required_address_info().goto_home_page())
#     #Get Password
#     password=cred.get_account_data()["password"]
#
#     yield username,email,password
#
#     #Delete Account
#     home=HomePage(page)
#     home.goto_delete_account().delete_account()
#     log.logger.info("Account Deleted Successfully!")