from pages.base.ae_base_page import AEBasePage


class PlaceOrderPage(AEBasePage):

    CONFIRM_MSG="order has been confirmed"

    def __init__(self,page):
        super().__init__(page)
        self.confirm_msg=self.page.get_by_text(self.CONFIRM_MSG,exact=False)


    def verify_confirm_order_msg(self):
        msg=self.get_text(self.confirm_msg)
        assert "order has been confirmed" in msg, f"Error: {msg}"
        return self