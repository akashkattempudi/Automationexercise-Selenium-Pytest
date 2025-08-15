# Selenium imports
from selenium.webdriver.remote.webdriver import WebDriver        # for type hinting 'driver'
from selenium.webdriver.common.by import By                       # for locating elements
from selenium.webdriver.support.ui import WebDriverWait           # for explicit waits
from selenium.webdriver.support import expected_conditions as EC   # for EC.visibility_of_element_located

# Your page object import
from selenium_tests.pages.products_page import products_page      # assuming products_page is defined here

class add_review_product_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_first_product(self):
        products = products_page(self.driver)
        products.click_products()
        products.click_view_product()
        return self

    def add_review(self, name, email, review):
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "review").send_keys(review)
        self.driver.find_element(By.ID, "button-review").click()
        return self

    def verify_success_message(self):
        success = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Thank you for your review')]"))
        )
        assert success.is_displayed(), "Review success message not visible"
        return self
