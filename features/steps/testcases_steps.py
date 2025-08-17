from behave import given, when, then
from selenium_tests.pages.page_test_cases import test_cases

@given("I am on the test cases page")
def step_impl(context):
    context.testcases_page = test_cases(context.driver)

@when("I click the test cases button")
def step_impl(context):
    context.testcases_page.click_test_cases_button()

@then("all test cases should be displayed and accessible")
def step_impl(context):
    context.testcases_page.verify_testcases()
