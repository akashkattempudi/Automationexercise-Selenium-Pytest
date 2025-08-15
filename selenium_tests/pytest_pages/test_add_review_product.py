# Import the page object
from selenium_tests.pages.add_review_product_page import add_review_product_page

def test_add_review_product(driver):
    # Initialize the page object and assign it to a variable
    review_page = add_review_product_page(driver)

    # Navigate to the first product
    review_page.navigate_to_first_product()

    # Add a review with name, email, and message
    review_page.add_review(
        "Reviewer",
        "reviewer@example.com",
        "Great product!"
    )

    # Verify that the success message is displayed
    review_page.verify_success_message()
