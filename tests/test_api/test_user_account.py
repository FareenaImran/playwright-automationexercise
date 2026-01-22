from api.end_points.account_api import AccountAPI


def test_create_user_account(api_request_context):
    """
    POST TEST
    Create new user account
    """
    account_api=AccountAPI(api_request_context)
    response=account_api.create_account()

    #assertion for creation
    assert response.status==200,f"Expected 200 but got {response.status}"

    json_response=response.json()
    message=json_response["message"]
    assert "created" in message.lower(),f"Error: Message : {message}"

    #get generated email
    email=account_api.get_email()
    print(f"\n{message} With Email: {email}")

def test_get_user_account_details(api_request_context,email="john.smith1769075170@example.com"):
    """
    GET Test
    Get user account details by email
    """
    account_api=AccountAPI(api_request_context)

    # get user account details by generated email
    response = account_api.get_user_detail_by_email(email)

    assert response.status == 200, f"Failed to get user details,Expected 200 but got {response.status}"

    # Verify user details by email
    details = response.json()
    if "email" in details["user"]:
        assert details["user"]["email"] == email, "Email Mismatch!!"

    print(f"\nUser with email: {email} exists in user records!")
    print("\n\nUser Detail:\n")
    for key,value in details["user"].items(): print(key,"-",value)


