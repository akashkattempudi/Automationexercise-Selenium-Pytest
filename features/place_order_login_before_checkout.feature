Feature: Place order after login before checkout

  Scenario: User logs in, adds product to cart, and proceeds to cart
    Given I am on the place order login before checkout page
    When I login first then proceed to checkout
    Then I should be able to view the cart with the added product
