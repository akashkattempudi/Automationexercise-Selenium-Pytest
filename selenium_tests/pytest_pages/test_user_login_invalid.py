from selenium_tests.pages.login_page_invalid import login_page
import time
def test_user_login(driver):
    login_test = login_page(driver)
    login_test.user_login_data()
    login_test.click_submit()


