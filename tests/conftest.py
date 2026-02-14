import os
from pathlib import Path
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from utils.save_navigation import block_ad
load_dotenv()

file_path=Path(__file__).resolve().parent
from utils.config_reader import read_config



#------------------------------------API's Fixtures----------------------------------------
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def api_request_context(playwright_instance):
        request_context=playwright_instance.request.new_context(timeout=60000)
        yield request_context
        request_context.dispose()


#------------------------------------UI's Fixtures----------------------------------------

@pytest.fixture(autouse=True)
def setup_module(page):
    page.wait_for_load_state("networkidle")
    page.goto(read_config(os.getenv("ENV"), "base_url"), timeout=150000)


@pytest.fixture(params=["chrome"],scope="function")
def browser(request,playwright_instance):
    browser_type=request.param
    if browser_type=="chrome":
        browser=playwright_instance.chromium.launch(headless=False,args=["--start-maximized"])
    elif browser_type=="firefox":
        browser=playwright_instance.firefox.launch(headless=False,args=["--start-maximized"])
    else:
        raise ValueError(f"Unsupported Browser : {browser_type}")
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context=browser.new_context(no_viewport=True)
    block_ad(context)
    page=context.new_page()
    yield page
    page.wait_for_timeout(2000)
    page.close()