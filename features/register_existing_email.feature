Feature: User registration with existing email

  Scenario: User tries to register with an email that already exists
    Given I am on the registration page
    When I enter registration details with an existing email
    And I submit the registration form
    Then I should see an email already exists message
