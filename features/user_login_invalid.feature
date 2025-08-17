Feature: User login with invalid credentials

    Scenario: User attempts to login with incorrect email or password
    Given I am on the login page for invalid login
    When I enter invalid login details
    And I submit the invalid login form
    Then I should see a login failure message
