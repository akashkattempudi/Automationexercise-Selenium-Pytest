from selenium_tests.pages.register_page_valid import register_page
def test_user_registration(driver):
    register_test = register_page(driver)
    register_test.user_register_data()
    register_test.user_form()
    register_test.create_account()
    register_test.click_to_continue()