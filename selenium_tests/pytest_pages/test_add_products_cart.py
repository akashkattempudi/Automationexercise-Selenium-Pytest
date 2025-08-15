from selenium_tests.pages.add_products_cart_page import add_products_cart_page
from selenium_tests.pages.verify_cart_quantity_page import verify_cart_quantity_page

def test_add_products_cart(driver):
    # Initialize the page object
    cart_page = add_products_cart_page(driver)

    # Add the first product to the cart
    cart_page.add_first_product_to_cart()

    # Click "Continue Shopping"
    cart_page.continue_shopping()

    # View the cart
    cart_page.view_cart()
