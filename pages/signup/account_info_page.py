from pages.base.ae_base_page import AEBasePage
from pages.signup.account_created_page import AccountCreatedPage
from pages.signup.signup_base import SignupBase
from utils.read_json import load_json


class AccountInfoPage(SignupBase):

    # ___________________________________Locators____________________________________________

    ACCOUNT_INFO="Enter Account Information"
    RADIO_MALE="Mr."
    RADIO_FEMALE="Mrs."
    PASSWORD_INPUT="#password"
    DAY="#days"
    MONTH="#months"
    YEAR="#years"
    ADDRESS_INFO_TEXT="Address Information"
    FIRST_NAME_INPUT="#first_name"
    LAST_NAME_INPUT="#last_name"
    ADDRESS_INPUT="#address1"
    STATE_INPUT="#state"
    CITY_INPUT="#city"
    ZIP_CODE_INPUT="#zipcode"
    MOBILE_NUM_INPUT="#mobile_number"
    CREATE_ACCOUNT_BTN="Create Account"

    def __init__(self,page):
        super().__init__(page)
        # self.account_info_text=self.page.get_by_role("heading",name=self.ACCOUNT_INFO)
        self.password_input=self.page.locator(self.PASSWORD_INPUT)
        self.first_name_input=self.page.locator(self.FIRST_NAME_INPUT)
        self.last_name_input=self.page.locator(self.LAST_NAME_INPUT)
        self.address_input=self.page.locator(self.ADDRESS_INPUT)
        self.state_input=self.page.locator(self.STATE_INPUT)
        self.city_input=self.page.locator(self.CITY_INPUT)
        self.zip_code_input=self.page.locator(self.ZIP_CODE_INPUT)
        self.mobile_num_input=self.page.locator(self.MOBILE_NUM_INPUT)

        # _________Credentials__________
        self._password=None

    # ___________________________________Methods____________________________________________


    def select_gender(self, gender):
        self.click(gender, self.RADIO_FEMALE if gender == "Mrs" else self.RADIO_MALE)
        return self

    def select_dob(self, day, month, year):
        self.select_dropdown("Day", self.DAY, day)
        self.select_dropdown("Month", self.MONTH, month)
        self.select_dropdown("Year", self.YEAR, year)
        return self

    def get_password(self):
        return self._password

    def enter_account_info(self):
        #Get Account Info from 'auth_data.json'
        account_info=self.get_account_data()
        #Verify Page Name
        self.verify_page_heading(self.ACCOUNT_INFO)
        #Gender
        self.select_gender(account_info["gender"])
        #Password
        self._password=account_info["password"]
        self.type("Password",self.password_input,account_info["password"],True)
        #Date of birth
        self.select_dob(account_info["birth_day"],account_info["birth_month"],account_info["birth_year"])
        return self

    def enter_required_address_info(self):
        # Get Address Info from 'auth_data.json'
        address_info = self.get_address_data()
        self.type("First Name",self.first_name_input,address_info["first_name"])
        self.type("Last Name",self.last_name_input,address_info["last_name"])
        self.type("Address",self.address_input,address_info["address"])
        self.type("State",self.state_input,address_info["state"])
        self.type("City",self.city_input,address_info["city"])
        self.type("Zip Code",self.zip_code_input,address_info["zip_code"])
        self.type("Mobile Num",self.mobile_num_input,address_info["mobile_num"],True)
        self.click("Create Account",self.CREATE_ACCOUNT_BTN)
        return AccountCreatedPage(self.page)




