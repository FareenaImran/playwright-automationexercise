from api.end_points.product_api import ProductAPI


def test_get_all_product_list(api_request_context):
    api=ProductAPI(api_request_context)
    response=api.get_all_products()
    assert response.status ==200, f"Expected 200, got {response.status}"

    json_response=response.json()

    assert "responseCode" in json_response,"Missing responseCode in response"
    assert "products" in json_response,"Missing products in response"

    #assert product list is not empty
    api.verify_list_not_empty(json_response,"products")

    products=json_response["products"]
    print(f"\nSuccessfully retrieved '{len(products)}' products!")