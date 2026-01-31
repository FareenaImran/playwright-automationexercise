import pytest

from api.end_points.account_api import AccountAPI
from pages.home.home_page import HomePage
from pages.signup.account_info_page import AccountInfoPage
from pages.signup.signup_login_page import SignupLoginPage


@pytest.fixture(scope="function")
def signup(page):
    try:
        #SignUp
        home = HomePage(page)
        (home.verify_home_page().go_to_signup_or_login().signup().
         enter_account_info().enter_required_address_info().goto_home_page())
        #Get username
        data = SignupLoginPage(page)
        username, email = data.get_signup_cred()
        #Get Password
        key=AccountInfoPage(page)
        password=key.get_password()

        yield username,email,password
    except Exception as e:
        raise Exception(f"\nFailed to Signup as new user {str(e)}")

