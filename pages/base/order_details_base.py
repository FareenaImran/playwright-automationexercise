import re

from pages.base.ae_base_page import AEBasePage


class OrderDetailsBase(AEBasePage):

    # __________________________________Locators____________________________________________

    CART_DESC="//*[@class='cart_description']"
    CART_PRICE=".cart_price"
    CART_QUANTITY=".cart_quantity"
    CART_TOTAL=".cart_total"

    def __init__(self,page):
        super().__init__(page)
        self.prod_desc = self.page.locator(self.CART_DESC)
        self.prod_price = self.page.locator(self.CART_PRICE)
        self.prod_quan = self.page.locator(self.CART_QUANTITY)
        self.prod_total = self.page.locator(self.CART_TOTAL)


    # ___________________________________Methods____________________________________________

    def get_all_products_desc(self):
        return self.get_text(self.prod_desc, True)

    def get_all_products_price(self):
        prices_text = self.get_text(self.prod_price, True)
        all_prices = [re.search(r'\d+', price).group() for price in prices_text]
        return all_prices

    def get_all_products_quantity(self):
        return self.get_text(self.prod_quan, True)

    def get_all_products_total(self):
        total_texts = self.get_text(self.prod_total, True)
        total_list = [re.search(r'\d+', total).group() for total in total_texts]
        return total_list

    def get_row_description(self,index):
        return self.get_text(self.page.locator(f"({self.CART_DESC})[{index}]"))