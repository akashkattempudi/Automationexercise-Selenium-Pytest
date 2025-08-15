
from selenium_tests.pages.subscription_home_page import subscription_home_page

from selenium_tests.pages.verify_cart_quantity_page import verify_cart_quantity_page

def test_verify_cart_quantity(driver):
    verify_cart_quantity_page(driver)\
        .view_product_and_add_quantity(3)\
        .verify_quantity_in_cart(3)