from pages.signup.account_info_page import AccountInfoPage
from pages.signup.signup_base import SignupBase


class SignupLoginPage(SignupBase):
    # ___________________________________Locators____________________________________________

    NEW_SIGNUP_TEXT = "New User Signup!"
    LOGIN_TO_ACCOUNT_TEXT = "Login to your account"
    SIGNUP_EMAIL_INPUT = "[data-qa='signup-email']"
    LOGIN_EMAIL_INPUT = "[data-qa='login-email']"
    NAME_INPUT = "Name"
    SIGNUP_BTN = "Signup"
    LOGIN_BTN = "Login"
    LOGIN_PASSWORD = "[data-qa='login-password']"
    ERROR = "//*[@style='color: red;']"

    # Credentials

    def __init__(self, page):
        super().__init__(page)
        self.name_input = self.page.get_by_placeholder(self.NAME_INPUT)
        self.signup_email_input = self.page.locator(self.SIGNUP_EMAIL_INPUT)
        self.login_email_input = self.page.locator(self.LOGIN_EMAIL_INPUT)
        self.login_password = self.page.locator(self.LOGIN_PASSWORD)
        self.errors = self.page.locator(self.ERROR)

    # ___________________________________Methods____________________________________________

    def verify_login_page(self):
        self.verify_page_heading(self.LOGIN_TO_ACCOUNT_TEXT)
        return self

    def verify_signup_page(self):
        self.verify_page_heading(self.NEW_SIGNUP_TEXT)
        return self

    def login(self, email, password):
        self.type("Email", self.login_email_input, email, True)
        self.type("Password", self.login_password, password, True)
        self.click("Login", self.LOGIN_BTN)
        return self

    def signup_user(self, name, email):
        self.type("Name", self.name_input, name)
        self.type("Email", self.signup_email_input, email, mask=True)
        self.click("Signup", self.SIGNUP_BTN)
        return AccountInfoPage(self.page)

    def get_validation_errors(self):
        error = self.get_text(self.errors)
        return error
