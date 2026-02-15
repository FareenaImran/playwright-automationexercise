from pages.base.ae_base_page import AEBasePage


class PlaceOrderPage(AEBasePage):

    CONFIRM_MSG="order has been confirmed"
    DOWNLOAD_BTN="Download Invoice"

    def __init__(self,page):
        super().__init__(page)
        self.confirm_msg=self.page.get_by_text(self.CONFIRM_MSG,exact=False)


    def verify_confirm_order_msg(self):
        msg=self.get_text(self.confirm_msg)
        assert "order has been confirmed" in msg, f"Error: {msg}"
        return self

    def download_invoice(self):
        try:
            with self.page.expect_download() as download_info:
                self.click("Download Invoice",self.DOWNLOAD_BTN)
            download=download_info.value
            return download
        except FileNotFoundError as e:
            raise Exception(str(e))



