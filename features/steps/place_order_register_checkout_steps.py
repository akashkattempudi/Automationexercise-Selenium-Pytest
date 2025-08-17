from behave import given, when, then
from selenium_tests.pages.place_order_register_checkout_page import place_order_register_checkout_page

@given("I am on the place order register checkout page")
def step_impl(context):
    context.checkout_page = place_order_register_checkout_page(context.driver)

@when("I add a product and checkout")
def step_impl(context):
    context.checkout_page.add_product_and_checkout()

@when('I register and place an order with name "{name}", card number "{card_number}", cvc "{cvc}", month "{month}", and year "{year}"')
def step_impl(context, name, card_number, cvc, month, year):
    payment_data = {
        "name": name,
        "card_number": card_number,
        "cvc": cvc,
        "month": month,
        "year": year
    }
    context.checkout_page.register_and_place_order(payment_data)

@then("I should see the order success message")
def step_impl(context):
    # The assertion is handled in register_and_place_order method
    pass
