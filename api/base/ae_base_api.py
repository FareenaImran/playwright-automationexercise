from api.base.base_api import BaseAPI


class AEBaseApi(BaseAPI):


    def verify_list_not_empty(self,json_data,key):
        try:
            data = json_data[key]
            assert isinstance(data, list), f"{key} should be a list"
            assert len(data) > 0, f"{key} list is empty"
            return self
        except :
            raise ValueError(f"Key Value > '{key}' is not correct")
