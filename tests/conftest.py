import pytest
from playwright.sync_api import sync_playwright


#------------------------------------API's Fixtures----------------------------------------

@pytest.fixture(scope="session")
def api_request_context():
    with sync_playwright() as p:
        request_context=p.request.new_context(timeout=60000)
        yield request_context
        request_context.dispose()


#------------------------------------UI's Fixtures----------------------------------------

@pytest.fixture(params=["chrome"],scope="function")
def browser(request):
    browser_type=request.param
    with sync_playwright() as p:
        if browser_type=="chrome":
            browser=p.chromium.launch(headless=False,args=["--start-maximized"])
        elif browser_type=="firefox":
            browser=p.firefox.launch(headless=False,args=["--start-maximized"])
        else:
            raise ValueError(f"Unsupported Browser : {browser_type}")
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context=browser.new_context()
    page=context.new_page()
    yield page
    page.wait_for_timeout(2000)
    page.close()