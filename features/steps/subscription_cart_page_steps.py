from behave import given, when, then
from selenium_tests.pages.subscription_cart_page import subscription_cart_page

@given("I am on the subscription cart page")
def step_impl(context):
    context.subscription_cart = subscription_cart_page(context.driver)

@when("I go to cart with a product")
def step_impl(context):
    context.subscription_cart.go_to_cart_with_product()

@when('I perform subscription steps with email "{email}"')
def step_impl(context, email):
    context.subscription_cart.subscription_steps(email)

@then("I should see the subscription success message")
def step_impl(context):
    # Success message verification is handled in subscription_steps method
    pass
