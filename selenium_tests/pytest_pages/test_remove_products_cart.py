from selenium_tests.pages.remove_products_cart_page import remove_products_cart_page

def test_remove_products_cart(driver):
    cart_page = remove_products_cart_page(driver)
    cart_page.add_product_to_cart()   # Ensure at least one product is in the cart
    cart_page.remove_all_products()   # Remove all products and verify
