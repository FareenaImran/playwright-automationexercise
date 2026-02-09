import logging

from pages.home.home_page import HomePage
from pages.signup.signup_base import SignupBase
from pages.signup.signup_login_page import SignupLoginPage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

def signup(page):
    #Get Signup Email and Username
    cred=SignupBase(page)
    username,email=cred.get_signup_data()
    #SignUp
    home = SignupLoginPage(page)
    home.signup_user(username,email).enter_account_info().enter_required_address_info().goto_home_page()
    #Get Password
    password=cred.get_account_data()["password"]
    return username,email,password

def delete_user(page):
    home = HomePage(page)
    home.goto_delete_account().verify_delete_account()
    log.logger.info("Account Deleted Successfully!")