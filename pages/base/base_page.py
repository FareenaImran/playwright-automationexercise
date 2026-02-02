import json
import logging
import os.path
from pathlib import Path

import allure
from playwright.sync_api import expect

from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class BasePage:
    BASE_DIR_PATH = file_path = os.path.dirname(os.path.abspath(__file__))
    IMAGE_PATH=os.path.join(BASE_DIR_PATH,'..',"..","test_data","images")

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
                    element.first.click()
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
            locator.scroll_into_view_if_needed()
            expect(locator).to_be_visible()
            log.logger.info(field_name+" "+"is visible")

    def select_dropdown(self,field_name,locator,option):
        with allure.step(f"Selecting {field_name} :{option}"):
            self.page.locator(locator).select_option(option)
            log.logger.info(f"Selecting {field_name} :{option}")
            return self

    def get_text(self,locator,is_list=False):
        if is_list:
            return locator.all_inner_texts()
        else:
            return locator.inner_text()

    def upload_image(self,field_name,btn_name,file_name):
        with allure.step(f"Uploading {file_name} ..."):
            file_path=os.path.join(self.IMAGE_PATH,file_name)
            with self.page.expect_file_chooser() as fc_info:
                self.click(field_name,btn_name)
            file_chooser=fc_info.value
            file_chooser.set_files(file_path)
            log.logger.info(f"Uploading {file_name} ... ")

    def accept_alert(self):
        self.page.once("dialog",lambda dialog:dialog.accept())
        return self

    def verify_url(self,text):
        with allure.step(f"Verifying {text} in page url"):
            assert text in self.page.url, f"Didn't get {text} in url"
            log.logger.info(f"Navigated to :{self.page.url}")
            return self

    def load_json(self,path):
        with open(path,"r") as f:
            return json.load(f)

