from selenium_tests.pages.products_page import products_page
def test_product_page(driver):
    product = products_page(driver)
    product.verify_home_page()
    product.click_products()
    product.verify_user_navigation()
    product.verify_products_is_visible()
    product.click_view_product()
    product.verify_on_product()
    product.verify_product_details()