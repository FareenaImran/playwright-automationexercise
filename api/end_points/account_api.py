import sys
import time
from pathlib import Path
from api.base.base_api import BaseAPI
from utils.read_json import load_json


class AccountAPI(BaseAPI):

    #-------------------------------URLs------------------------------
    CREATE_ACCOUNT_URL="api/createAccount"
    ACCOUNT_DETAILS_URL="api/getUserDetailByEmail"
    UPDATE_ACCOUNT_URL="api/updateAccount"
    DELETE_ACCOUNT_URL="api/deleteAccount"

    JSON_PATH=Path(__file__).resolve().parent.parent/"payload"/"create_user.json"

    def __init__(self,request_context):
        super().__init__(request_context)
        self._RANDOM_EMAIL=None
        self._last_payload=None

    def _generate_random_email(self):
        payload = load_json(self.JSON_PATH)
        payload["email"] = payload["email"].replace("{random}", str(int(time.time())))
        self._RANDOM_EMAIL= payload["email"]
        return payload

    def get_email(self):
        if self._RANDOM_EMAIL:
            return self._RANDOM_EMAIL
        return None

    def get_payload(self):
        return self._last_payload.copy()

    def create_account(self):
        payload=self._generate_random_email()
        self._last_payload=payload.copy()
        return self.post(self.CREATE_ACCOUNT_URL,payload)

    def get_user_detail_by(self,key,value):
        response=self.get(self.ACCOUNT_DETAILS_URL,{key:value})
        return response
    
    def update_account_details(self,update_data):
        response=self.put(self.UPDATE_ACCOUNT_URL,update_data)
        assert response.status == 200, f"Failed to update user details,Expected 200 but got {response.status}"
        return response.json()

    def delete_user_account(self,email,password):
        response=self.delete(self.DELETE_ACCOUNT_URL,{"email":email,"password":password})
        assert response.status == 200, "Unable to delete user account"
        return response.json()