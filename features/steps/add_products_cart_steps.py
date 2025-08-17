from behave import given, when, then
from selenium_tests.pages.add_products_cart_page import add_products_cart_page

@given("I am on the add products cart page")
def step_impl(context):
    context.cart_page = add_products_cart_page(context.driver)

@when("I add the first product to the cart")
def step_impl(context):
    context.cart_page.add_first_product_to_cart()

@when("I click Continue Shopping")
def step_impl(context):
    context.cart_page.continue_shopping()

@when("I view the cart")
def step_impl(context):
    context.cart_page.view_cart()

@then("the product should be visible in the cart")
def step_impl(context):
    # You can add additional assertion logic here if the page object provides it
    # For example: context.cart_page.verify_product_is_in_cart()
    pass
