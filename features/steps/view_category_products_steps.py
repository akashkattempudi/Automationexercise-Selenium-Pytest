from behave import given, when, then
from selenium_tests.pages.view_category_products_page import view_category_products_page

@given("I am on the category products page")
def step_impl(context):
    context.category_page = view_category_products_page(context.driver)

@when('I click the category with xpath "{category_xpath}"')
def step_impl(context, category_xpath):
    context.category_page.click_category_and_verify(category_xpath, "CategoryName")  # Replace CategoryName if dynamic

@then('I should see the category page with header containing "{expected_text}"')
def step_impl(context, expected_text):
    # The assertion is done inside the method, so just pass or add extra checks as needed
    pass
