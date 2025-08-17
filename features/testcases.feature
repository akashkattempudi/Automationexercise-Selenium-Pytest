Feature: View and verify all test cases

  Scenario: User clicks the Test Cases button and verifies all test cases are visible and clickable
    Given I am on the test cases page
    When I click the test cases button
    Then all test cases should be displayed and accessible
