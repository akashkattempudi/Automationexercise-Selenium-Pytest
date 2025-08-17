Feature: Place order after registration before checkout

  Scenario: User registers, adds product to cart, then proceeds to checkout
    Given I am on the place order register before checkout page
    When I register first then proceed to checkout
    Then I should be on the checkout page with the product in cart
