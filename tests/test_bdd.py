import pytest
from pytest_bdd import scenario, given, when, then
from my_module import login_user, reset_password, update_user_profile  # Assuming functions are implemented

@pytest.fixture
def valid_user_for_update():
    return {"username": "valid_user", "email": "user@example.com"}


# BDD Test for User Login (1)
@scenario('feature/add_task.feature', 'Successful login with valid credentials')
def test_successful_login():
    pass

@given('the user has a valid username and password')
def valid_credentials():
    return {"username": "valid_username", "password": "valid_password"}

@when('the user attempts to log in')
def user_login(valid_credentials):
    result = login_user(valid_credentials["username"], valid_credentials["password"])
    return result

@then('the user should be logged in successfully')
def check_login_success(user_login):
    assert user_login["status"] == "success"

# BDD Test for Failed User Login (2)
@scenario('feature/add_task.feature', 'Failed login with invalid credentials')
def test_failed_login():
    pass

@given('the user has an invalid username and password')
def invalid_credentials():
    return {"username": "invalid_username", "password": "invalid_password"}

@when('the user attempts to log in')
def user_login_fail(invalid_credentials):
    return login_user(invalid_credentials["username"], invalid_credentials["password"])

@then('the user should see a login failed message')
def check_login_failed(user_login_fail):
    assert user_login_fail["status"] == "failed"
    assert user_login_fail["error"] == "Invalid credentials"

# BDD Test for Password Reset (3)
@scenario('feature/add_task.feature', 'Successful password reset for a valid username')
def test_successful_password_reset():
    pass

@given('the user has a valid username')
def valid_username_for_reset():
    return "valid_username"

@when('the user requests a password reset')
def request_password_reset(valid_username_for_reset):
    return reset_password(valid_username_for_reset, "new_password")

@then('the user should see a password reset successful message')
def check_password_reset_success(request_password_reset):
    assert request_password_reset["status"] == "success"
    assert request_password_reset["message"] == "Password reset successful"

# BDD Test for Failed Password Reset (non-existent username) (4)
@scenario('feature/add_task.feature', 'Failed password reset for a non-existent username')
def test_failed_password_reset():
    pass

@given('the user has a non-existent username')
def invalid_username_for_reset():
    return "non_existent_username"

@when('the user requests a password reset')
def request_password_reset_fail(invalid_username_for_reset):
    return reset_password(invalid_username_for_reset, "new_password")

@then('the user should see a username not found message')
def check_password_reset_failure(request_password_reset_fail):
    assert request_password_reset_fail["status"] == "failed"
    assert request_password_reset_fail["error"] == "Username not found"

# BDD Test for User Profile Update (5)
@scenario('feature/add_task.feature', 'Successful user profile update')
def test_successful_profile_update():
    pass

@given('the user has a valid username and wants to update their profile')
def valid_user_for_update():
    return {"username": "valid_user", "new_email": "new_email@example.com"}

@when('the user updates their profile')
def update_profile(valid_user_for_update):
    return update_user_profile(valid_user_for_update["username"], {"email": valid_user_for_update["new_email"]})

@then('the user should see a profile updated successfully message')
def check_profile_update_success(update_profile):
    assert update_profile["status"] == "success"
    assert update_profile["message"] == "Profile updated successfully"

