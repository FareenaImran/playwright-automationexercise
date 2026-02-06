from pages.base.ae_base_page import AEBasePage


class SignupBase(AEBasePage):
    def __init__(self,page):
        super().__init__(page)
        self.auth_data=self.load_json("test_data/auth_data.json")


    def get_signup_data(self):
        signup_info = self.auth_data["Signup_Data"]["signup_info"]
        return signup_info["username"],signup_info["email"]

    def get_account_data(self):
        account_info = self.auth_data["Signup_Data"]["account_info"]
        return account_info

    def get_address_data(self):
        address_info = self.auth_data["Signup_Data"]["address_info"]
        first_name = address_info["first_name"]
        last_name = address_info["last_name"]
        address = address_info["address"]
        state = address_info["state"]
        city = address_info["city"]
        zip_code = address_info["zip_code"]
        number = address_info["mobile_num"]
        return first_name,last_name,address,state,city,zip_code,number

    def get_login_cred(self):
        cred=self.auth_data["Login_Data"]
        return cred["username"],cred["email"],cred["password"]