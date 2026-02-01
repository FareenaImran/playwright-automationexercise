import logging

from pages.home.home_page import HomePage
from pages.signup.signup_base import SignupBase
from pages.signup.signup_login_page import SignupLoginPage
from tests.base_test import BaseTest
from utils.log_util import Logger
from tests.fixtures.ui_fixtures import signup

log=Logger(__name__,logging.INFO)
class TestRegistration(BaseTest):

    def test_signup(self,page,signup):
        """
        Test User Registration and
        Delete Account Flow
        """
        #Signup
        username,_,_=signup

        #Verify Logged in username
        home=HomePage(page)
        home.verify_logged_in_username(username)

        log.logger.info("Signup Successfully!")

    def test_register_user_with_existing_email(self, page):
        """
        Test validation errors when user signup with already registered email
        """
        # Get registered Credentials
        cred = SignupBase(page)
        username, email, _ = cred.get_login_cred()

        # Signup
        home = HomePage(page)
        home.go_to_signup_or_login().verify_signup_page().signup_user(username,email)

        #Verify Validation Error
        validation=SignupLoginPage(page)
        error_msg=validation.get_validation_errors()

        assert "already exist" in error_msg,"Didn't get any validation error"

        log.logger.info(f"Error: {error_msg}")
