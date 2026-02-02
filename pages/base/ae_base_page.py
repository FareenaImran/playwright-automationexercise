import logging
import allure
from playwright.sync_api import expect
from pages.base.base_page import BasePage
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class AEBasePage(BasePage):

    # ___________________________________Locators____________________________________________
    CLOSE_ICON = ".close"
    MODAL =".modal-content"
    SUCCESS_MSG=".alert-success"


    def __init__(self,page):
        super().__init__(page)
        self.modal=self.page.locator(self.MODAL)
        self.success_msg=self.page.locator(self.SUCCESS_MSG)

    # ___________________________________Methods____________________________________________

    def verify_page(self,option_name,is_selected=None):
        with allure.step(f"Selected navbar option : {option_name}"):
            locator=self.page.get_by_role("link",name=option_name)
            has_style=locator.get_attribute("style")
            if is_selected:
                assert has_style=="color: orange;"
                log.logger.info(f"Selected navbar option : {option_name}")
                return True
            else:
                return False

    def verify_page_heading(self,value):
        with allure.step(f"On Page: {value}"):
            heading=self.page.get_by_role("heading",name=value)
            heading.wait_for(state="visible")
            assert heading.is_visible(),f"Unable to navigate to {value}"
            log.logger.info(f"On Page : {value}")
            return heading.inner_text()

    def close_modal_if_present(self):
        """Close modal if present"""
        if self.modal.is_visible():
            self.click("Close",self.CLOSE_ICON)

    def get_alert_msg(self):
        alert = self.get_text(self.success_msg)
        return alert

    def get_validation_msg(self,field_name,locator):
        msg=locator.evaluate("element => element.validationMessage")
        return msg

