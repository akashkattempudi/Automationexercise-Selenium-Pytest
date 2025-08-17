from behave import given, when, then
from selenium_tests.pages.login_page_valid import login_page

@given("I am on the login page")
def step_impl(context):
    context.login_test = login_page(context.driver)

@when("I enter valid login details")
def step_impl(context):
    context.login_test.user_login_data()

@when("I submit the login form")
def step_impl(context):
    context.login_test.click_submit()

@then("I should be logged in successfully")
def step_impl(context):
    # For real verification, you could check a welcome message or user dashboard, depending on your site.
    pass
