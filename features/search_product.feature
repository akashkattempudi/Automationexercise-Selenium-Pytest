Feature: Search products

  Scenario: User searches for a product by name
    Given I am on the search products page
    When I navigate to the products page
    And I enter the product name "Men Tshirt" and search
    Then the searched products should be visible
    And all searched products should be displayed
