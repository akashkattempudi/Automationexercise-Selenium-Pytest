Feature: User logout functionality

  Scenario: User logs in and logs out successfully
    Given I am on the logout page
    When I login as a valid user
    And I click the logout button
    Then I should be logged out successfully
