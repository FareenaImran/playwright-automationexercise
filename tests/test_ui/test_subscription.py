import logging

import pytest

from pages.home.home_page import HomePage
from tests.base_test import BaseTest
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

class TestProducts(BaseTest):

    subscription_data={
        ("abc@gmail.com","subscribed"),
        ("","please fill"),
        ("None","please include")
    }

    @pytest.mark.parametrize("email,msg",subscription_data)
    def test_subscription(self,page,email,msg):
        """
        Verify subscription
        """
        home = HomePage(page)
        result=home.verify_home_page().goto_footer().subscribe(email).verify_subscription()
        assert msg in result.lower(),f"Didn't get any alert msg"
        log.logger.info(result)
