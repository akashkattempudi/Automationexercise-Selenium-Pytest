Feature: Subscription functionality on cart page

  Scenario: User adds product to cart and subscribes with email
    Given I am on the subscription cart page
    When I go to cart with a product
    And I perform subscription steps with email "cart@example.com"
    Then I should see the subscription success message
