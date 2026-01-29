import json
import logging
import allure
from playwright.sync_api import expect

from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class BasePage:

    def __init__(self,page):
        self.page=page

    #--------------------------Methods------------------------------

    def click(self,field_name,value):
        """Click on element when visible"""
        with allure.step(f"Clicking on '{field_name}'"):
            elements=[
                self.page.get_by_role("button", name=value),
                self.page.get_by_text(value,exact=True),
                self.page.get_by_role("link", name=value),
                self.page.get_by_role("radio", name=value),
                self.page.locator(value)
            ]

            for element in elements:
                try:
                    element.wait_for(state="visible",timeout=2000)
                    element.scroll_into_view_if_needed()
                    element.click()
                    log.logger.info("Clicking on " + field_name)
                    return  #exit function
                except:
                    continue
            raise Exception(f"Unable to locate : {field_name}")

    def type(self,field_name,locator,value,mask=False):
        with allure.step("Typing " + field_name):
            try:
                locator.wait_for(state="visible")
                locator.type(value)
                if mask:
                    log.logger.info("Entering " + field_name + " : *****************")
                else:
                    log.logger.info("Entering " + field_name + " : " + value)
            except:
                raise Exception(f"Unable to locate : {field_name}")

    def is_visible(self,field_name,locator):
        with allure.step(field_name + "is visible"):
            expect(locator).to_be_visible()
            log.logger.info(field_name+" "+"is visible")

    def select_dropdown(self,field_name,locator,option):
        with allure.step(f"Selecting {field_name} :{option}"):
            self.page.locator(locator).select_option(option)
            log.logger.info(f"Selecting {field_name} :{option}")
            return self

    def get_text(self,locator):
        return locator.inner_text()

    def load_json(self,path):
        with open(path,"r") as f:
            return json.load(f)

