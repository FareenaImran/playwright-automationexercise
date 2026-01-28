import pytest

from api.end_points.product_api import ProductAPI

@pytest.fixture(scope="function")
def get_product_list(api_request_context):
    api = ProductAPI(api_request_context)
    response = api.get_all_products()
    assert response.status == 200, f"Expected 200 but got {response.status}"
    yield response.json()

