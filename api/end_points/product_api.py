from api.base.ae_base_api import AEBaseApi


class ProductAPI(AEBaseApi):

    PRODUCTS_URL="api/productsList"

    def get_all_products(self):
        return self.get(self.PRODUCTS_URL)
    
