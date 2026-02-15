from pages.base.ae_base_page import AEBasePage


class FooterPage(AEBasePage):

    #-----------------------------------Locators------------------------------------------
    SUBS_EMAIL_INPUT="#susbscribe_email"
    SUBS_BTN="#subscribe"


    def __init__(self,page):
        super().__init__(page)
        self.subs_email_input=self.page.locator(self.SUBS_EMAIL_INPUT)

    #-----------------------------------Methods------------------------------------------

    def subscribe(self,email):
        if email:
            self.type("Email",self.subs_email_input,email,True)
        self.click("Subscribe Icon",self.SUBS_BTN)
        return self

    def verify_subscription(self):
        msg=self.get_validation_msg(self.subs_email_input)
        return msg if msg else self.get_alert_msg()




