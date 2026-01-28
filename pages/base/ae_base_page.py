from pages.base.base_page import BasePage


class AEBasePage(BasePage):

    # ___________________________________Locators____________________________________________
    CLOSE_ICON = ".close"
    MODAL =".modal-content"

    def __init__(self,page):
        super().__init__(page)
        self.modal=self.page.locator(self.MODAL)


    # ___________________________________Methods____________________________________________

    def verify_page(self,option_name,is_selected=None):
        locator=self.page.get_by_role("link",name=option_name)
        has_style=locator.get_attrbute("style")
        if is_selected:
            assert has_style=="color: orange;"
            return True
        else:
            return False


    def close_modal_if_present(self):
        """Close modal if present"""
        if self.modal.is_visible():
            self.click("Close",self.CLOSE_ICON)