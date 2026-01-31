from pages.home.home_page import HomePage
from tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test_login_with_valid_credentials(self,page):
        """Test that user is allowed to log in with correct email and password"""
        home=HomePage(page)
        try:
            (home.verify_home_page().go_to_signup_or_login().login())
        except Exception as e:
            raise Exception(f"Unable to login {str(e)}")

