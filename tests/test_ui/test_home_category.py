import logging
from pages.home.home_page import HomePage
from tests.base_test import BaseTest
from utils.log_util import Logger

log= Logger(__name__, logging.INFO)

class TestCategory(BaseTest):

    def test_product_category_navigates_to_correct_page(self,page):
        """Test Clicking on product category navigates to correct page """
        total_main_category=3    #Women , Men and Kinds
        home=HomePage(page)
        for i in range(1,total_main_category+1):
            #Get main category text
            _,category=home.click_on_category(i).get_category_text(i)
            _,count = home.get_sub_categories_count()
            for j in range(1,count+1):
                #Click on Main Category
                page_obj,sub_category = home.select_sub_category(j)
                #Get page heading text
                page_heading=page_obj.get_page_heading()
                #Verify Category and Sub Category Text in page heading
                assert (category.lower() and sub_category.lower()) in page_heading.lower(),f"Page Heading {page_heading}"
                if j==count:
                    break
                #Click on main Category
                home.click_on_category(i)
                log.logger.info(f"Category :{category} , Sub Category: {sub_category} contains in Page Heading :'{page_heading}'")
        log.logger.info("Verified! All Category Navigates to Correct Page")