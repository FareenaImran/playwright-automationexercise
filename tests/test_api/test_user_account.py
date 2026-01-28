import logging

import pytest

from api.end_points.account_api import AccountAPI
from tests.fixtures.api_fixtures.account_fixtures import create_account,get_account_details
from utils.log_util import Logger

log=Logger(__name__,logging.INFO)

@pytest.mark.account_api
def test_create_user_account(api_request_context,create_account):
    """
    POST TEST
    Create new user account
    """
    user_data=create_account
    log.logger.info(f"\nPOST: Account created with '{user_data['email']}'")

@pytest.mark.account_api
def test_get_user_account_details(api_request_context,get_account_details):
    """
    GET Test
    Get user account details by email
    """
    email = "john.smith1769075170@example.com"
    details=get_account_details(email)

    # Verify user details by emai
    log.logger.info(f"\nUser Details: \n\n {details}")

@pytest.mark.account_api
def test_put_account_details(api_request_context,create_account,get_account_details):
    """
    TEST PUT
    Test update user details
    """
    user_data=create_account
    email=user_data["email"]
    log.logger.info(f"\nCreated Account with {email}")

    #Update user info
    account_api=AccountAPI(api_request_context)
    updated_payload=user_data.copy()
    updated_payload["name"],updated_payload["city"],updated_payload["country"]="Fareena","Karachi","Pakistan"

    json_response=account_api.update_account_details(updated_payload)

    assert "updated" in json_response["message"],"Unable to update user details"
    log.logger.info(f'\n{json_response["message"]}')

    details=get_account_details(email)
    log.logger.info(f'\n{details}')

@pytest.mark.account_api
def test_delete_user_account(api_request_context,create_account):
    """
    Test 'Delete'
    Test 'delete' user account
    """
    #Create user account
    user_data = create_account
    email = user_data["email"]
    password=user_data["password"]
    log.logger.info(f"\nCreated Account with {email}")

    #delete user account
    api_account=AccountAPI(api_request_context)
    response=api_account.delete_user_account(email,password)

    #Verify response message
    message=response["message"]
    assert "deleted" in message , f"Expected account deleted but got {message}"
    log.logger.info(message)

@pytest.mark.account_api
def test_post_to_verify_login_with_valid_details(api_request_context,create_account):
    """
    Test 'POST'
    Test post to verify logging with email and password
    """
    #Create Account
    user_data = create_account
    email,password=user_data["email"],user_data["password"]

    #Verify User
    account_api=AccountAPI(api_request_context)
    response=account_api.verify_user(email,password)

    #Verify Response Code and Msg
    assert response["responseCode"]==200,f"Expected 200 but got {response['responseCode']}"
    assert "User exists" in response["message"],f"{response['message']}"

    #Output
    log.logger.info(f"\n{response['message']}")

@pytest.mark.account_api
def test_post_to_verify_login_without_email_parameter(api_request_context, create_account):
    """
    Test 'POST'
    Test post to verify logging without email
    """
    # Create Account
    user_data = create_account
    password = user_data["password"]

    # Verify User
    account_api = AccountAPI(api_request_context)
    response = account_api.verify_user(None,password)

    # Verify Response Code and Msg
    assert response["responseCode"] == 400, f"Expected 400 but got {response['responseCode']}"
    assert "missing" in response["message"], f"{response['message']}"

    # Output
    log.logger.info(f"\n{response['message']}")

