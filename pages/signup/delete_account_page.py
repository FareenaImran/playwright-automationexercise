from pages.base.ae_base_page import AEBasePage

class DeleteAccountPage(AEBasePage):

    ACCOUNT_DELETE_TEXT="Account Deleted"

    def __init__(self,page):
        super().__init__(page)


    def get_account_deleted_msg(self):
        success_msg=self.verify_page_heading(self.ACCOUNT_DELETE_TEXT)
        return success_msg.lower()

    def delete_account(self):
        msg=self.get_account_deleted_msg()
        assert ("deleted" or "DELETED") in msg,f"\nUnexpected Message :{msg}"
        return self
