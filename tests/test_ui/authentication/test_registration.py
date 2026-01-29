import logging
from pages.home.home_page import HomePage
from pages.signup.signup_login_page import SignupLoginPage
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)
class TestRegistration(BaseTest):

    def test_signup_and_delete_account(self,page):
        """
        Test User Registration and
        Delete Account Flow
        """
        home = HomePage(page)
        try:
            #SignUp
            (home.verify_home_page().go_to_signup_or_login().signup().
            enter_account_info().enter_required_address_info().
            goto_home_page())
            #Get username
            data=SignupLoginPage(page)
            username,_=data.get_signup_cred()
            #Verify Logged in username
            home.verify_logged_in_username(username)
        except Exception as e:
            raise Exception(f"\nFailed to Signup as new user {str(e)}")

        #Delete Account
        account_deleted_msg=home.goto_delete_account().get_account_deleted_msg()
        assert "ACCOUNT DELETED" in account_deleted_msg,f"\nUnexpected Message :{account_deleted_msg}"

        log.logger.info(f"Account Deleted Successfully!! Got Message: {account_deleted_msg}")




