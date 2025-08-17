from behave import given, when, then
from selenium_tests.pages.login_page_invalid import login_page

@given("I am on the login page for invalid login")
def step_impl(context):
    context.login_test = login_page(context.driver)

@when("I enter invalid login details")
def step_impl(context):
    context.login_test.user_login_data()

@when("I submit the invalid login form")
def step_impl(context):
    context.login_test.click_submit()

@then("I should see a login failure message")
def step_impl(context):
    pass
