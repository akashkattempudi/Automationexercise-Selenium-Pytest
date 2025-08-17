Feature: View and verify brand products

  Scenario: User clicks a brand and verifies the brand page header
    Given I am on the brand products page
    When I click the brand with xpath "//a[contains(text(),'BrandName')]"
    Then I should see the brand page with header containing "BrandName"
