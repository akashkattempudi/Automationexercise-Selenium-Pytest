from selenium.webdriver.common.by import By


from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class test_cases:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    def click_test_cases_button(self):
        wait = WebDriverWait(self.driver, 10)
        locator =(By.CSS_SELECTOR, "a[href='/test_cases']")
        wait.until(EC.element_to_be_clickable(locator)).click()

    def verify_testcases(self):
        tests = [
            "Test Case 1: Register User",
            "Test Case 2: Login User with correct email and password",
            "Test Case 3: Login User with incorrect email and password",
            "Test Case 4: Logout User",
            "Test Case 5: Register User with existing email",
            "Test Case 6: Contact Us Form",
            "Test Case 7: Verify Test Cases Page",
            "Test Case 8: Verify All Products and product detail page",
            "Test Case 9: Search Product",
            "Test Case 10: Verify Subscription in home page",
            "Test Case 11: Verify Subscription in Cart page",
            "Test Case 12: Add Products in Cart",
            "Test Case 13: Verify Product quantity in Cart",
            "Test Case 14: Place Order: Register while Checkout",
            "Test Case 15: Place Order: Register before Checkout",
            "Test Case 16: Place Order: Login before Checkout",
            "Test Case 17: Remove Products From Cart",
            "Test Case 18: View Category Products",
            "Test Case 19: View & Cart Brand Products",
            "Test Case 20: Search Products and Verify Cart After Login",
            "Test Case 21: Add review on product",
            "Test Case 22: Add to cart from Recommended items",
            "Test Case 23: Verify address details in checkout page",
            "Test Case 24: Download Invoice after purchase order",
            "Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality",
            "Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality"
        ]
        for test_case in tests:
            xpath = f'//u[normalize-space()="{test_case}"]'
            element = self.driver.find_element(By.XPATH, xpath)
            from selenium.webdriver.support.wait import WebDriverWait
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            assert element.is_displayed(), f"{test_case} not visible"
            element.click()
            element.click()

