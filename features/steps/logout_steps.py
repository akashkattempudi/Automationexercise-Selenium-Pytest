from behave import given, when, then
from selenium_tests.pages.logout_page import logout_page

@given("I am on the logout page")
def step_impl(context):
    context.logout = logout_page(context.driver)

@when("I login as a valid user")
def step_impl(context):
    context.logout.login_user_page()

@when("I click the logout button")
def step_impl(context):
    context.logout.logout_user_page()

@then("I should be logged out successfully")
def step_impl(context):
    # You can implement and call a verification method,
    # e.g., context.logout.verify_logged_out(), if you have one
    pass
