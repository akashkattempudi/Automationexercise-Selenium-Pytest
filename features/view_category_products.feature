Feature: View and verify category products

  Scenario: User clicks a category and verifies the category page header
    Given I am on the category products page
    When I click the category with xpath "//a[contains(text(),'CategoryName')]"
    Then I should see the category page with header containing "CategoryName"
