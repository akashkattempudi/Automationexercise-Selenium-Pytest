Feature: Products page interactions

  Scenario: User navigates and verifies products page and product details
    Given I am on the products page
    When I verify the home page
    And I click products
    And I verify user navigation
    And I verify products are visible
    And I view a product
    And I verify the user is on the product page
    And I verify product details
    Then the product details should be displayed correctly
