from pages.base.ae_base_page import AEBasePage

class DeleteAccountPage(AEBasePage):

    ACCOUNT_DELETE_TEXT="Account Deleted"

    def __init__(self,page):
        super().__init__(page)


    def verify_delete_account(self):
        msg=self.get_page_heading()
        assert "deleted" in msg.lower(),f"\nUnexpected Message :{msg}"
        return self
