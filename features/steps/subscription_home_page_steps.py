from behave import given, when, then
from selenium_tests.pages.subscription_home_page import subscription_home_page

@given("I am on the subscription home page")
def step_impl(context):
    context.subscription_page = subscription_home_page(context.driver)

@when("I scroll to the subscription section")
def step_impl(context):
    context.subscription_page.scroll_to_subscription()

@when("I verify the subscription heading is visible")
def step_impl(context):
    context.subscription_page.verify_subscription_visible()

@when('I enter email "{email}" and submit')
def step_impl(context, email):
    context.subscription_page.enter_email_and_submit(email)

@then("Then I should see the subscription success message on the home page")
def step_impl(context):
    context.subscription_page.verify_success_message()
