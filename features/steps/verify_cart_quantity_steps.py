from behave import given, when, then
from selenium_tests.pages.verify_cart_quantity_page import verify_cart_quantity_page

@given("I am on the verify cart quantity page")
def step_impl(context):
    context.cart_quantity_page = verify_cart_quantity_page(context.driver)

@when("I view product and add quantity {quantity:d}")
def step_impl(context, quantity):
    context.cart_quantity_page.view_product_and_add_quantity(quantity)

@then("I verify the quantity in cart is {expected_qty:d}")
def step_impl(context, expected_qty):
    context.cart_quantity_page.verify_quantity_in_cart(expected_qty)
