import sys
import time
from pathlib import Path
from api.base.base_api import BaseAPI
from utils.read_json import load_json


class AccountAPI(BaseAPI):

    CREATE_ACCOUNT_URL="api/createAccount"
    ACCOUNT_DETAILS_URL="api/getUserDetailByEmail"
    UPDATE_ACCOUNT_URL="api/updateAccount"
    JSON_PATH=Path(__file__).resolve().parent.parent/"payload"/"create_user.json"

    def __init__(self,request_context):
        super().__init__(request_context)
        self._RANDOM_EMAIL=None

    def _generate_random_email(self):
        payload = load_json(self.JSON_PATH)
        payload["email"] = payload["email"].replace("{random}", str(int(time.time())))
        self._RANDOM_EMAIL= payload["email"]
        return payload,self._RANDOM_EMAIL

    def get_email(self):
        if self._RANDOM_EMAIL:
            return self._RANDOM_EMAIL
        return None

    def create_account(self):
        payload,email=self._generate_random_email()
        return self.post(self.CREATE_ACCOUNT_URL,payload)

    def get_user_detail_by_email(self,email):
        response=self.get(self.ACCOUNT_DETAILS_URL,params={"email":email})
        return response
    
    def update_account_details_partial(self,params):
        response=self.patch(self.UPDATE_ACCOUNT_URL,params=params)
        return response