from behave import given, when, then
from selenium_tests.pages.place_order_register_before_checkout_page import place_order_register_before_checkout_page

@given("I am on the place order register before checkout page")
def step_impl(context):
    context.checkout_page = place_order_register_before_checkout_page(context.driver)

@when("I register first then proceed to checkout")
def step_impl(context):
    context.checkout_page.register_first_then_checkout()

@then("I should be on the checkout page with the product in cart")
def step_impl(context):
    # Add verification step if you have any (like page title, url check etc)
    pass
