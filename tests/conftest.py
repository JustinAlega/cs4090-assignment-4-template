
import pytest

@pytest.fixture
def invalid_credentials():
    return {"username": "invalid_user", "password": "wrongpassword"}

@pytest.fixture
def user_login():
    # Return a mocked successful login response
    return {"status": "success", "username": "test_user"}

@pytest.fixture
def user_login_fail():
    # Return a mocked failed login response
    return {"status": "failed", "error": "Invalid credentials"}

@pytest.fixture
def invalid_username_for_reset():
    # Logic to simulate an invalid username for password reset
    return {"username": "nonexistent_user"}

@pytest.fixture
def invalid_username_for_reset():
    # Return a mock user with an invalid username
    return {"username": "invalid_user_for_reset"}

@pytest.fixture
def request_password_reset():
    # Return a mocked successful password reset response
    return {"status": "success", "message": "Password reset successful"}


@pytest.fixture
def request_password_reset_fail():
    # Return a mocked failed password reset response
    return {"status": "failed", "error": "Username not found"}


@pytest.fixture
def valid_user_for_update():
    return {
        'email': 'user@example.com',
        'username': 'valid_user',
        'new_email': 'newuser@example.com'
    }

@pytest.fixture
def update_profile():
    # Return a mocked successful profile update response
    return {"status": "success", "message": "Profile updated successfully"}
