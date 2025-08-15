from selenium_tests.pages.page_test_cases import test_cases
def test_page_test_case(driver):
    test = test_cases(driver)
    test.click_test_cases_button()
    test.verify_testcases()