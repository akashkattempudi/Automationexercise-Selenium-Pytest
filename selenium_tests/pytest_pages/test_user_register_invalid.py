from selenium_tests.pages.register_page_invalid import register_page
def test_user_registration(driver):
    register_test = register_page(driver)
    register_test.user_register_data()
