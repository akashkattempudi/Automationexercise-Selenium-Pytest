from behave import given, when, then
from selenium_tests.pages.search_products_cart_after_login_page import search_products_cart_after_login_page

@given("I am on the search products cart after login page")
def step_impl(context):
    context.search_page = search_products_cart_after_login_page(context.driver)

@when("I go to products")
def step_impl(context):
    context.search_page.go_to_products()

@when('I search for product "{name}"')
def step_impl(context, name):
    context.search_page.search_product(name)

@when("I add products to cart")
def step_impl(context):
    context.search_page.add_products_to_cart()

@when("I go to cart")
def step_impl(context):
    context.search_page.go_to_cart()

@when("I login")
def step_impl(context):
    context.search_page.login()

@then("the cart items should be verified")
def step_impl(context):
    context.search_page.verify_cart_items()
