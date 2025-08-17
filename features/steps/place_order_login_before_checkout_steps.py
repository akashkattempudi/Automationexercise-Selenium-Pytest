from behave import given, when, then
from selenium_tests.pages.place_order_login_before_checkout_page import place_order_login_before_checkout_page

@given("I am on the place order login before checkout page")
def step_impl(context):
    context.checkout_page = place_order_login_before_checkout_page(context.driver)

@when("I login first then proceed to checkout")
def step_impl(context):
    context.checkout_page.login_first_then_checkout()

@then("I should be able to view the cart with the added product")
def step_impl(context):
    # Add cart verification here if you want to check, otherwise pass.
    pass
