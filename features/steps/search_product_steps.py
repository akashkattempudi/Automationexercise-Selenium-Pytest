from behave import given, when, then
from selenium_tests.pages.search_product import search_products_page

@given("I am on the search products page")
def step_impl(context):
    context.search = search_products_page(context.driver)

@when("I navigate to the products page")
def step_impl(context):
    context.search.navigate_to_products_page()

@when('I enter the product name "{name}" and search')
def step_impl(context, name):
    context.search.enter_product_name_and_search(name)

@then("the searched products should be visible")
def step_impl(context):
    context.search.verify_searched_products_visible()

@then("all searched products should be displayed")
def step_impl(context):
    context.search.verify_all_searched_products_are_visible()
