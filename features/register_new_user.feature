Feature: Register a new user account

  Scenario: User registers with valid unique email and completes the form
    Given I am on the registration page for a new user
    When I enter valid registration details
    And I fill the registration form completely
    And I create the account successfully
    And I click to continue after registration
    Then I should be registered successfully
