Feature: Search products and add to cart after login

  Scenario: User searches "T-shirt", adds products to cart, logs in, and verifies cart items
    Given I am on the search products cart after login page
    When I go to products
    And I search for product "T-shirt"
    And I add products to cart
    And I go to cart
    And I login
    Then the cart items should be verified
