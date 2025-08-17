Feature: Verify product quantity in cart

  Scenario: User sets product quantity and verifies it in the cart
    Given I am on the verify cart quantity page
    When I view product and add quantity 3
    Then I verify the quantity in cart is 3
