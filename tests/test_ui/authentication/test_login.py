import logging
from pages.home.home_page import HomePage
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
        home.logout()

        #Login
        home.go_to_signup_or_login().login(email,password)

        #Verify Username
        success_msg=home.verify_logged_in_username(username)

        log.logger.info(f"Logged In Successfully: {success_msg}")

    def test_login_with_invalid_credentials(self,page):
        """
        Test validation errors when user login with invalid credentials
        """
        #Login
        home=HomePage(page)
        error_msg=home.go_to_signup_or_login().login("invalid@gmail.com","000").get_validation_errors()
        assert "incorrect" in error_msg

        log.logger.info(f"Validation Error(s): {error_msg}")




