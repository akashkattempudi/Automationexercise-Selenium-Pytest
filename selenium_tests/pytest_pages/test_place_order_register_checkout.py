from selenium_tests.pages.subscription_home_page import subscription_home_page
from selenium_tests.pages.verify_cart_quantity_page import verify_cart_quantity_page
from selenium_tests.pages.place_order_register_checkout_page import place_order_register_checkout_page

def test_place_order_register_checkout(driver):
    payment_data = {
        "name": "Test User",
        "card_number": "4111111111111111",
        "cvc": "123",
        "month": "12",
        "year": "2025"
    }

    # Initialize page object
    place_order_page = place_order_register_checkout_page(driver)

    # Perform actions
    place_order_page.add_product_and_checkout()
    place_order_page.register_and_place_order(payment_data)
