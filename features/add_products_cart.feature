Feature: Add products to cart

  Scenario: User adds the first product to cart and views the cart
    Given I am on the add products cart page
    When I add the first product to the cart
    And I click Continue Shopping
    And I view the cart
    Then the product should be visible in the cart
