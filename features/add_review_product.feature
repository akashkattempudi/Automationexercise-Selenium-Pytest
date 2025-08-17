Feature: Add product review

  Scenario: User adds a review for a product successfully
    Given I am on the add review product page
    When I navigate to the first product
    And I add a review with name "Reviewer", email "reviewer@example.com", and message "Great product!"
    Then I should see a success message for the review
