import logging

from pages.home.home_page import HomePage
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestContactUs(BaseTest):

    def test_contact_us_form(self,page):
        """
        Test that user is allowed to submit contact us form with correct details
        """
        home=HomePage(page)

        #Fill Form and Get Success Msg
        message=(home.goto_contact_us().
                 verify_get_in_touch_text().
                 fill_form("Fareena","farina@gmail.com","Test","Hello..")
                 .get_success_msg())

        #Verify Success Msg
        assert "submitted" in message,f"Unable to submit contact us form"

        log.logger.info(message)

