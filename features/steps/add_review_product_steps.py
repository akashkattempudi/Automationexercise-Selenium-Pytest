from behave import given, when, then
from selenium_tests.pages.add_review_product_page import add_review_product_page

@given("I am on the add review product page")
def step_impl(context):
    context.review_page = add_review_product_page(context.driver)

@when("I navigate to the first product")
def step_impl(context):
    context.review_page.navigate_to_first_product()

@when('I add a review with name "{name}", email "{email}", and message "{message}"')
def step_impl(context, name, email, message):
    context.review_page.add_review(name, email, message)

@then("I should see a success message for the review")
def step_impl(context):
    context.review_page.verify_success_message()
