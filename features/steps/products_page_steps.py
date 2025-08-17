from behave import given, when, then
from selenium_tests.pages.products_page import products_page

@given("I am on the products page")
def step_impl(context):
    context.products = products_page(context.driver)

@when("I verify the home page")
def step_impl(context):
    context.products.verify_home_page()

@when("I click products")
def step_impl(context):
    context.products.click_products()

@when("I verify user navigation")
def step_impl(context):
    context.products.verify_user_navigation()

@when("I verify products are visible")
def step_impl(context):
    context.products.verify_products_is_visible()

@when("I view a product")
def step_impl(context):
    context.products.click_view_product()

@when("I verify the user is on the product page")
def step_impl(context):
    context.products.verify_on_product()

@when("I verify product details")
def step_impl(context):
    context.products.verify_product_details()

@then("the product details should be displayed correctly")
def step_impl(context):
    # You can add any assertion or further validation here if needed
    pass
