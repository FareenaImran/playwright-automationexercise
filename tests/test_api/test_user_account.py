from api.end_points.account_api import AccountAPI
from tests.fixtures.api_fixtures import create_account
from tests.fixtures.api_fixtures import get_account_details


def test_create_user_account(create_account):
    """
    POST TEST
    Create new user account
    """
    user_data=create_account
    print(f"\nPOST: Account created with '{user_data['email']}'")

def test_get_user_account_details(api_request_context,get_account_details):
    """
    GET Test
    Get user account details by email
    """
    email = "john.smith1769075170@example.com"
    details=get_account_details(email)

    # Verify user details by emai
    print(f"\nUser Details: \n\n {details}")

def test_put_account_details(api_request_context,create_account,get_account_details):
    """
    TEST PUT
    Test update user details
    """
    user_data=create_account
    email=user_data["email"]
    print(f"\nCreated Account with {email}")

    #Update user info
    account_api=AccountAPI(api_request_context)
    updated_payload=user_data.copy()
    updated_payload["name"],updated_payload["city"],updated_payload["country"]="Fareena","Karachi","Pakistan"

    response=account_api.update_account_details(updated_payload)
    assert response.status==200, f"Failed to update user details,Expected 200 but got {response.status}"

    assert "updated" in response.json()["message"],"Unable to update user details"
    print(f'\n{response.json()["message"]}')

    details=get_account_details(email)
    print(f'\n{details}')

def test_delete_user_account(api_request_context,create_account):
    """
    Test 'Delete'
    Test 'delete' user account
    """
    #Create user account
    user_data = create_account
    email = user_data["email"]
    password=user_data["password"]
    print(f"\nCreated Account with {email}")

    #delete user account
    api_account=AccountAPI(api_request_context)
    response=api_account.delete_user_account(email,password)
    assert response.status==200, "Unable to delete user account"

    #Verify response message
    message=response.json()["message"]
    assert "deleted" in message , f"Expected account deleted but got {message}"
    print(message)

