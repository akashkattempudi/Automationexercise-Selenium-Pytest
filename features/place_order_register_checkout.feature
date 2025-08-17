Feature: Place order after registration with checkout and payment

  Scenario: User registers, places order with payment details
    Given I am on the place order register checkout page
    When I add a product and checkout
    And I register and place an order with name "Test User", card number "4111111111111111", cvc "123", month "12", and year "2025"
    Then I should see the order success message
