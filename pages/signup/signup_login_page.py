from pages.signup.account_info_page import AccountInfoPage
from pages.signup.signup_base import SignupBase


class SignupLoginPage(SignupBase):

    # ___________________________________Locators____________________________________________

    NEW_SIGNUP="New User Signup!"
    SIGNUP_EMAIL_INPUT="[data-qa='signup-email']"
    NAME_INPUT="Name"
    SIGNUP_BTN="Signup"
    LOGIN_BTN="Login"

    def __init__(self,page):
        super().__init__(page)
        self.new_user_signup=self.page.get_by_role("heading",name=self.NEW_SIGNUP)
        self.name_input=self.page.get_by_placeholder(self.NAME_INPUT)
        self.email_input=self.page.locator(self.SIGNUP_EMAIL_INPUT)
        self._email=None
        self._name=None

    # ___________________________________Methods____________________________________________

    def login(self):
        pass


    def signup(self):
        #Get Data from 'auth_data.json'
        self._name,self._email=self.get_signup_cred()

        self.is_visible("New User Signup!",self.new_user_signup)
        self.type("Name",self.name_input,self._name)
        self.type("Email", self.email_input, self._email,mask=True)
        self.click("Signup",self.SIGNUP_BTN)
        return AccountInfoPage(self.page)


    def get_signup_cred(self):
        data=self.get_signup_data()
        self._name,self._email=data["username"],data["email"]
        return self._name,self._email

