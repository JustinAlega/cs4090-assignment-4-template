import pytest
from my_module import login_user, reset_password, update_user_profile

# Feature 1: User Authentication (Login)

# Test for successful login
def test_user_login_valid_credentials():
    response = login_user("valid_username", "valid_password")
    assert response == True

# Test for failed login
def test_user_login_invalid_credentials():
    response = login_user("invalid_username", "invalid_password")
    assert response == False

# Feature 2: Password Reset

# Test for successful password reset
def test_password_reset_success():
    response = reset_password("valid_username", "new_password")
    assert response == "Password for valid_username has been reset to new_password"


# Test for failed password reset (username not found)
def test_password_reset_failure():
    response = reset_password("non_existent_username", "new_password")
    assert response == "Password for non_existent_username has been reset to new_password"

# Feature 3: User Profile Update

# Test for successful user profile update
def test_update_user_profile_success():
    response = update_user_profile("valid_username", {"email": "new_email@example.com"})
    assert response == "Profile for valid_username updated with {'email': 'new_email@example.com'}"

# Test for failed user profile update (username not found)
def test_update_user_profile_failure():
    response = update_user_profile("non_existent_username", {"email": "new_email@example.com"})
    assert response == "Profile for non_existent_username updated with {'email': 'new_email@example.com'}"
