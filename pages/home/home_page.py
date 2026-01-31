import logging
from pages.base.ae_base_page import AEBasePage
from pages.signup.delete_account_page import DeleteAccountPage
from pages.signup.signup_login_page import SignupLoginPage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class HomePage(AEBasePage):
    # ___________________________________Locators____________________________________________

    #------Menu Options------
    TESTCASES="Test Cases"
    HOME="Home"
    SIGNUP_LOGIN="Signup / Login"
    DELETE_ACCOUNT="Delete Account"
    LOGGED_IN_USERNAME_TEXT="Logged in as"
    LOGOUT="Logout"

    def __init__(self,page):
        super().__init__(page)
        self.test_cases=self.page.get_by_role("link",name=self.TESTCASES)
        self.logged_in_username_text=self.page.get_by_text(self.LOGGED_IN_USERNAME_TEXT)

    # ___________________________________Methods____________________________________________

    def verify_home_page(self):
        """ Verify that home page is visible successfully"""
        self.verify_page(self.HOME,is_selected=True)
        return self

    def go_to_signup_or_login(self):
        """Navigate to Sign/Login Page"""
        self.click("Signup/Login",self.SIGNUP_LOGIN)
        return SignupLoginPage(self.page)

    def logout(self):
        self.click("Logout",self.LOGOUT)
        return SignupLoginPage(self.page)

    def verify_logged_in_username(self,username):
        """Verify that username after signup display on home page """
        try:
            logged_in_as_username=self.get_text(self.logged_in_username_text)
            assert username in logged_in_as_username, f"\nDid not get username '{username}' on home page "
            return logged_in_as_username
        except Exception as e:
            raise Exception(f"Failed to login/sign {str(e)}")

    def goto_delete_account(self):
        """Delete user account after signup"""
        self.click("Delete Account", self.DELETE_ACCOUNT)
        return DeleteAccountPage(self.page)





