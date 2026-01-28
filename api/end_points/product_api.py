import os.path
from re import search

from api.base.ae_base_api import AEBaseApi
from utils.read_json import load_json


class ProductAPI(AEBaseApi):

    #-----------------------------URL's----------------------------
    def __init__(self,request_context):
        super().__init__(request_context)
        self.PRODUCTS_URL="api/productsList"
        self.BRAND_URL="api/brandsList"
        self.SEARCH_PROD_URL="api/searchProduct"

    #-----------------------------File Paths-----------------------
    END_POINTS_DIR=os.path.dirname(os.path.abspath(__file__))
    PROD_PATH=os.path.join(END_POINTS_DIR,"..","payload","product_info.json")

    def get_all_products(self):
        response = self.get(self.PRODUCTS_URL)
        return response.json()

    def get_all_brand_list(self):
        response=self.get(self.BRAND_URL)
        return response.json()

    def add_product(self):
        payload=load_json(self.PROD_PATH)["PRODUCT_INFO"]
        response = self.post(self.PRODUCTS_URL, payload)
        return response.json()

    def add_brand(self):
        payload = load_json(self.PROD_PATH)["BRAND_INFO"]
        response = self.post(self.PRODUCTS_URL, payload)
        return response.json()

    def search_product(self,term=None):
        if term:
            response = self.post(self.SEARCH_PROD_URL, {'search_product':term})
        else:
            response = self.post(self.SEARCH_PROD_URL, {})
        return response.json()
