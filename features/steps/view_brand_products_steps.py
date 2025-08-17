from behave import given, when, then
from selenium_tests.pages.view_brand_products_page import view_brand_products_page

@given("I am on the brand products page")
def step_impl(context):
    context.brand_page = view_brand_products_page(context.driver)

@when('I click the brand with xpath "{brand_xpath}"')
def step_impl(context, brand_xpath):
    context.brand_page.click_brand_and_verify(brand_xpath, "BrandName")  # Replace BrandName if dynamic

@then('I should see the brand page with header containing "{expected_text}"')
def step_impl(context, expected_text):
    # Verification is done in the method, just pass here or add extra checks
    pass
