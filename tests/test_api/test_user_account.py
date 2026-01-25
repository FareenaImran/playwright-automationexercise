from api.end_points.account_api import AccountAPI
from tests.fixtures.api_fixtures import create_account

def test_create_user_account(api_request_context,create_account):
    """
    POST TEST
    Create new user account
    """
    user_data=create_account
    print(f"\nPOST: Account created with '{user_data['email']}'")

def test_get_user_account_details(api_request_context,email="john.smith1769075170@example.com"):
    """
    GET Test
    Get user account details by email
    """
    account_api=AccountAPI(api_request_context)
    response = account_api.get_user_detail_by("email",email)

    assert response.status == 200, f"Failed to get user details,Expected 200 but got {response.status}"

    # Verify user details by email
    details = response.json()
    if "email" in details["user"]:
        assert details["user"]["email"] == email, "Email Mismatch!!"

    print(f"\nUser with email: {email} exists in user records!")
    print("\n\nUser Detail:\n")
    for key,value in details["user"].items(): print(key,"-",value)

def test_put_account_details(api_request_context,create_account):
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

    response=account_api.get_user_detail_by("email",email)
    print(f'\n{response.json()["user"]}')

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

