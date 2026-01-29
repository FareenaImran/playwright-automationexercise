from pages.base.ae_base_page import AEBasePage


class AccountCreatedPage(AEBasePage):

    ACCOUNT_CREATED_TEXT="Account Created!"
    CONTINUE_BTN="Continue"

    def __init__(self,page):
        super().__init__(page)


    def goto_home_page(self):
        self.verify_page_heading(self.ACCOUNT_CREATED_TEXT)
        self.click("Continue",self.CONTINUE_BTN)
        return self



