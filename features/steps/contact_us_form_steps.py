from behave import given, when, then
from selenium_tests.pages.contact_us_form import contact_us_form

@given("I am on the homepage")
def step_impl(context):
    context.contact = contact_us_form(context.driver)

@when("I click the Contact Us button")
def step_impl(context):
    context.contact.click_contact_us_button()

@when("I fill the Contact Us form")
def step_impl(context):
    context.contact.fill_contact_us_form()

@when("I click the Submit button")
def step_impl(context):
    context.contact.click_submit_button()

@then("I should see a success message for contact form submission")
def step_impl(context):
    pass
