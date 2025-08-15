from selenium_tests.pages.search_product import search_products_page
def test_search_products_page(driver):
    search = search_products_page(driver)
    search.navigate_to_products_page()
    search.enter_product_name_and_search("Men Tshirt")
    search.verify_searched_products_visible()
    search.verify_all_searched_products_are_visible()