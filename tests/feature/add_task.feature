Feature: User Login, Password Reset, and Profile Update

  Scenario: Successful login with valid credentials
    Given the user has a valid username and password
    When the user attempts to log in
    Then the user should be logged in successfully

  Scenario: Failed login with invalid credentials
    Given the user has an invalid username and password
    When the user attempts to log in
    Then the user should see a login failed message

  Scenario: Successful password reset for a valid username
    Given the user has a valid username
    When the user requests a password reset
    Then the user should see a password reset successful message

  Scenario: Failed password reset for a non-existent username
    Given the user has a non-existent username
    When the user requests a password reset
    Then the user should see a username not found message

  Scenario: Successful user profile update
    Given the user has a valid username and wants to update their profile
    When the user updates their profile
    Then the user should see a profile updated successfully message
