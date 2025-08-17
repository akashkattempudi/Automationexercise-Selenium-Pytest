Feature: User login with valid credentials

  Scenario: User logs in with correct email and password
    Given I am on the login page
    When I enter valid login details
    And I submit the login form
    Then I should be logged in successfully
