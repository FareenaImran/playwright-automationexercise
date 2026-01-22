import json
from difflib import restore
from pathlib import Path

file_path=Path(__file__).resolve().parent
from utils.config_reader import read_config



class BaseAPI:
    def __init__(self,request_context):
            self.request=request_context

    def get(self,end_point,params=None):
        return self.request.get(f"{read_config('basic_info','base_url')}{end_point}",params=params)

    def post(self,end_point,payload):
        return self.request.post(f"{read_config('basic_info','base_url')}{end_point}",form=payload)

    def put(self,end_point,params=None):
        return self.request.put(f"{read_config('basic_info', 'base_url')}{end_point}", params=params)

    def patch(self,end_point,params=None):
        return self.request.patch(f"{read_config('basic_info', 'base_url')}{end_point}", params=params)

    def delete(self,end_point,params=None):
        return self.request.delete(f"{read_config('basic_info', 'base_url')}{end_point}", params=params)


