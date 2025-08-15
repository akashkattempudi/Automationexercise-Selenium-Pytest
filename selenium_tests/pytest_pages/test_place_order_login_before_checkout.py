

from selenium_tests.pages.place_order_login_before_checkout_page import place_order_login_before_checkout_page


def test_place_order_login_before_checkout(driver):
    place_order_page = place_order_login_before_checkout_page(driver)
    place_order_page.login_first_then_checkout()
