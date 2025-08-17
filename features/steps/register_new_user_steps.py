from behave import given, when, then
from selenium_tests.pages.register_page_valid import register_page

@given("I am on the registration page for a new user")
def step_impl(context):
    context.register = register_page(context.driver)

@when("I enter valid registration details")
def step_impl(context):
    context.register.user_register_data()

@when("I fill the registration form completely")
def step_impl(context):
    context.register.user_form()

@when("I create the account successfully")
def step_impl(context):
    context.register.create_account()

@when("I click to continue after registration")
def step_impl(context):
    context.register.click_to_continue()

@then("I should be registered successfully")
def step_impl(context):
    context.register.verify_registration()
