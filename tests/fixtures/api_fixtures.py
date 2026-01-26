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

@pytest.fixture(scope="session")
def get_account_details(api_request_context):

    def _get_email(email):
        account_api = AccountAPI(api_request_context)
        response = account_api.get_user_detail_by("email", email)
        #Assertion to fetch details
        assert response.status == 200, f"Failed to get user details,Expected 200 but got {response.status}"
        # Verify user details by email
        details = response.json()["user"]
        assert details["email"] == email, "Email Mismatch!!"
        return details

    yield _get_email

