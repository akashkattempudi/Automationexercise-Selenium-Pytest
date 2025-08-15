# Selenium imports
from selenium.webdriver.remote.webdriver import WebDriver        # for type hinting 'driver'
from selenium.webdriver.common.by import By                       # for locating elements
from selenium.webdriver.support.ui import WebDriverWait           # for explicit waits
from selenium.webdriver.support import expected_conditions as EC   # for EC.element_to_be_clickable

# Your page object imports
from selenium_tests.pages.products_page import products_page      # assuming products_page is defined here

class add_products_cart_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_product_to_cart(self):
        products = products_page(self.driver)
        products.verify_home_page()
        products.click_products()
        products.verify_user_navigation()
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'add-to-cart')])[1]"))
        )
        add_btn.click()
        return self

    def continue_shopping(self):

        # Wait for the Continue Shopping button inside the modal to be clickable
        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block"))
        )

        # Scroll into view just in case
        self.driver.execute_script("arguments[0].scrollIntoView(true);", continue_btn)
        continue_btn.click()
        return self

    def view_cart(self):
        cart_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/view_cart']"))
        )
        cart_btn.click()
        return self
