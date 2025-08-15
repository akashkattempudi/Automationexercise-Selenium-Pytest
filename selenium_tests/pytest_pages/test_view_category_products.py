
from selenium_tests.pages.subscription_home_page import subscription_home_page

from selenium_tests.pages.verify_cart_quantity_page import verify_cart_quantity_page

from selenium_tests.pages.view_category_products_page import view_category_products_page

def test_view_category_products(driver):
    view_category_products_page(driver)\
        .click_category_and_verify("//a[text()='Women']", "Women")