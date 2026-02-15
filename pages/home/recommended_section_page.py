from pages.products.product_base_page import ProductBasePage


class RecommendedSectionPage(ProductBasePage):
    #------------------------------Locators---------------------------------------
    ADD_CART_TO_BTN="//a[contains(@class,'add-to-cart')]"
    RECOMMENDED_PROD="//*[contains(@id,'recommended')]"
    PRODUCT_NAME="//p"



    def __init__(self,page):
        super().__init__(page)


    #------------------------------Methods-----------------------------------------
    def add_to_cart(self,index):
        add_to_cart = f"({self.RECOMMENDED_PROD}{self.ADD_CART_TO_BTN})[{index}]"
        self.click("Add to cart", add_to_cart)
        return self

    def get_product_name(self, index_no):
        product=f"({self.RECOMMENDED_PROD}{self.PRODUCT_NAME})[{index_no}]"
        product_name = self.page.locator(product)
        return self.get_text(product_name)


