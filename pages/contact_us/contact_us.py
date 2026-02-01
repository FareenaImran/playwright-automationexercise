from pages.base.ae_base_page import AEBasePage


class ContactUsPage(AEBasePage):
    #----------------------------------Locators-----------------------------------------
    GET_IN_TOUCH_TEXT="Get In Touch"
    NAME="[data-qa='name']"
    EMAIL="[data-qa='email']"
    SUBJECT="[data-qa='subject']"
    MSG="[data-qa='message']"
    UPLOAD_BTN="[type='file'][name='upload_file']"
    SUBMIT_BTN="[data-qa='submit-button']"
    SUCCESS_MSG=".status.alert.alert-success"

    def __init__(self,page):
        super().__init__(page)
        self.name_input=self.page.locator(self.NAME)
        self.email_input=self.page.locator(self.EMAIL)
        self.subject_input=self.page.locator(self.SUBJECT)
        self.msg_input=self.page.locator(self.MSG)
        self.upload_btn=self.page.locator(self.UPLOAD_BTN)
        self.success_msg=self.page.locator(self.SUCCESS_MSG)


    #----------------------------------Methods-----------------------------------------

    def verify_get_in_touch_text(self):
        self.verify_page_heading(self.GET_IN_TOUCH_TEXT)
        return self

    def fill_form(self,name,email,subject,msg):
        try:
            self.type("Name",self.name_input,name)
            self.type("Email",self.email_input,email,True)
            self.type("Subject",self.subject_input,subject)
            self.type("Message",self.msg_input,msg)
            self.upload_image("Choose File",self.UPLOAD_BTN,"image1.jpg")
            self.accept_alert()
            self.click("submit",self.SUBMIT_BTN)
            return self
        except Exception as e:
            raise Exception(f"Unable to fill contact us form.. {str(e)}")

    def get_success_msg(self):
        msg=self.get_text(self.success_msg)
        return msg





