from selenium_tests.pages.logout_page import logout_page
def test_logout(driver):
    logout= logout_page(driver)
    logout.login_user_page()
    logout.logout_user_page()