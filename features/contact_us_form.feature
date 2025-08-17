Feature: Contact Us form submission

  Scenario: User submits the Contact Us form successfully
    Given I am on the homepage
    When I click the Contact Us button
    And I fill the Contact Us form
    And I click the Submit button
    Then I should see a success message for contact form submission
