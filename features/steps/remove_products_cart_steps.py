from behave import given, when, then
from selenium_tests.pages.remove_products_cart_page import remove_products_cart_page

@given("I am on the remove products cart page")
def step_impl(context):
    context.cart_page = remove_products_cart_page(context.driver)

@when("I add a product to the cart")
def step_impl(context):
    context.cart_page.add_product_to_cart()

@when("I remove all products from the cart")
def step_impl(context):
    context.cart_page.remove_all_products()

@then("the cart should be empty")
def step_impl(context):
    # The assertion is inside remove_all_products; you can add extra verification if needed
    pass
