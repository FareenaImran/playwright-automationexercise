import logging

from pages.home.home_page import HomePage
from tests.base_test import BaseTest
from utils.log_util import Logger
from tests.fixtures.ui_fixtures import signup

log=Logger(__name__,logging.INFO)
class TestRegistration(BaseTest):

    def test_signup_and_delete_account(self,page,signup):
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





