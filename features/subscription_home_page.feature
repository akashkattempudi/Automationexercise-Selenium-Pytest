Feature: Subscription functionality on home page

  Scenario: User subscribes from the home page successfully
    Given I am on the subscription home page
    When I scroll to the subscription section
    And I verify the subscription heading is visible
    And I enter email "home@example.com" and submit
    Then Then I should see the subscription success message on the home page

