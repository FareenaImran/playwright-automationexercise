import logging
from pages.base.ae_base_page import AEBasePage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class HomePage(AEBasePage):
    # ___________________________________Locators____________________________________________

    #------Menu Options------
    TESTCASES="Test Cases"
    HOME="Home"


    def __init__(self,page):
        super().__init__(page)
        self.test_cases=self.page.get_by_role("link",name=self.TESTCASES)


    # ___________________________________Methods____________________________________________

    def verify_home_page(self):
        self.verify_page(self.HOME,is_selected=True)
        return True




