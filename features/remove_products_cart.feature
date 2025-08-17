Feature: Remove products from cart

  Scenario: User adds a product to the cart and then removes all products
    Given I am on the remove products cart page
    When I add a product to the cart
    And I remove all products from the cart
    Then the cart should be empty
