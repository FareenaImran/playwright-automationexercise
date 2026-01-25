import pytest

from api.end_points.account_api import AccountAPI

@pytest.fixture(scope="session")
def create_account(api_request_context):
    account_api=AccountAPI(api_request_context)
    response=account_api.create_account()
    # assertion for creation
    assert response.status in [200, 201], f"Account creation failed!: {response.status}"
    # Get the generated email
    payload = account_api.get_payload()
    yield payload

