import logging
from pages.home.home_page import HomePage
from pages.signup.signup_base import SignupBase
from tests.fixtures.ui_fixtures import signup
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestLogin(BaseTest):
    def test_login_with_valid_credentials(self,page,signup):
        """
        Test that user is allowed to log in with correct email and password
        """
        #Signup
        username,email,password=signup
        home=HomePage(page)
        home.logout_user()

        #Login
        home.go_to_signup_or_login().verify_login_page().login(email,password)

        #Verify Username
        home.verify_logged_in_username(username)

        log.logger.info(f"Logged In Successfully")

    def test_login_with_invalid_credentials(self,page):
        """
        Test validation errors when user login with invalid credentials
        """
        #Login
        home=HomePage(page)
        error_msg=home.go_to_signup_or_login().verify_login_page().login("invalid@gmail.com","000").get_validation_errors()
        assert "incorrect" in error_msg

        log.logger.info(f"Validation Error(s): {error_msg}")

    def test_logout(self,page):
        """
        Test that logout navigates to login page
        """
        #Get Credentials
        cred=SignupBase(page)
        username,email,password=cred.get_login_cred()
        #Login
        home=HomePage(page)
        home.go_to_signup_or_login().verify_login_page().login(email,password)
        home.verify_logged_in_username(username).logout_user().verify_login_page()

        log.logger.info(f"Logout Successfully")



