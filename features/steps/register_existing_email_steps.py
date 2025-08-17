from behave import given, when, then
from selenium_tests.pages.register_page_valid import register_page

@given("I am on the registration page")
def step_impl(context):
    context.register = register_page(context.driver)

@when("I enter registration details with an existing email")
def step_impl(context):
    # This method fills in the name and existing email
    context.register.user_register_data()

@when("I submit the registration form")
def step_impl(context):
    # The submit button click is part of user_register_data
    pass

@then("I should see an email already exists message")
def step_impl(context):
    # The assertion and print are also in user_register_data,
    # so you can extend the page object to raise or return for robust checks.
    pass
