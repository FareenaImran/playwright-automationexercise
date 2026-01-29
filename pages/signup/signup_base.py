from pages.base.ae_base_page import AEBasePage


class SignupBase(AEBasePage):
    def __init__(self,page):
        super().__init__(page)
        self.auth_data=self.load_json("test_data/auth_data.json")


    def get_signup_data(self):
        signup_info = self.auth_data["Signup_Data"]["signup_info"]
        return signup_info

    def get_account_data(self):
        account_info = self.auth_data["Signup_Data"]["account_info"]
        return account_info

    def get_address_data(self):
        address_info = self.auth_data["Signup_Data"]["address_info"]
        return address_info