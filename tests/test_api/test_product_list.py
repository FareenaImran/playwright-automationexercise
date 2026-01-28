import pytest
from api.end_points.product_api import ProductAPI
from tests.fixtures.api_fixtures.product_fixtures import get_product_list

@pytest.mark.product_api
def test_get_all_product_list(api_request_context,get_product_list):
    json_response = get_product_list
    assert "products" in json_response,"Expected product list"
    print(f"\n{json_response}")

@pytest.mark.product_api
def test_product_info(api_request_context,get_product_list):
    json_response = get_product_list
    #Get Products info list
    products=json_response["products"]
    #Verify Product Info
    for product in products:
        assert product["id"],f"Product Name: '{product['name']}'> 'id' is missing"
        assert product["name"],f"Product ID: '{product['id']}'> 'name' is missing"
        assert product["price"],f"Product Name: '{product['name']}'> 'price' is missing"
        assert product["brand"],f"Product Name: '{product['name']}'> 'brand info' is missing"
        assert product["category"],f"Product Name: '{product['name']}'> 'category info' is missing"

@pytest.mark.product_api
def test_post_to_all_products_list(api_request_context):
    product_api=ProductAPI(api_request_context)
    response=product_api.add_product()
    #Verify Response Code
    assert response["responseCode"]==405,f"Expected 405 but got {response['responseCode']}"
    #Verify Response Message
    assert "not supported" in response["message"],f"Expected Msg: 'This request method is not supported' but got {response['message']}"
    print(f"\nMessage: {response}")

def test_get_all_brand_list(api_request_context):
    brand=ProductAPI(api_request_context)
    response=brand.get_all_brand_list()
    #Verify Response Code
    assert response["responseCode"]==200,f"Expected 200 but got {response['responseCode']}"
    #Band List Output
    brand_list=[print(f"\n{brand_info}") for brand_info in response['brands']]
    print(f"\nTotal Brands:{len(brand_list)}")

def test_post_to_all_brands_list(api_request_context):
    brand = ProductAPI(api_request_context)
    response = brand.add_brand()
    # Verify Response Code
    assert response["responseCode"] == 405, f"Expected 405 but got {response['responseCode']}"
    # Verify Response Message
    assert "not supported" in response["message"], f"Expected Msg: 'This request method is not supported' but got {response['message']}"
    print(f"\nMessage: {response}")

def test_post_to_search_product_without_parameter(api_request_context):
    """
    Test : Post To Search Product Without
    Request Parameter
    """
    search=ProductAPI(api_request_context)
    response=search.search_product()
    #Verify Response Code
    assert response["responseCode"]==400,f"Expected 400 but got {response['responseCode']}"
    #Result
    print(f"\n{response}")

def test_post_to_search_product(api_request_context):
    """
    Test : Post To Search Product With 
    Request Parameter : search_product
    """
    search=ProductAPI(api_request_context)
    response=search.search_product("top")
    #Verify Response Code
    assert response["responseCode"]==200,f"Expected 200 but got {response['responseCode']}"
    #Output Searched Products List
    searched_list=[print(f"\n{search_item}") for search_item in response["products"]]
    print(f"\n\nTotal Searched Products: {len(searched_list)}")




