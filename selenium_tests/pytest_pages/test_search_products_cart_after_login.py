from selenium_tests.pages.search_products_cart_after_login_page import search_products_cart_after_login_page

def test_search_products_cart_after_login(driver):
    search_page = search_products_cart_after_login_page(driver)
    search_page.go_to_products()
    search_page.search_product("T-shirt")
    search_page.add_products_to_cart()
    search_page.go_to_cart()
    search_page.login()
    search_page.verify_cart_items()
