# Selenium imports
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import the add products page
from selenium_tests.pages.add_products_cart_page import add_products_cart_page

class remove_products_cart_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self):
        """Add the first product to cart using the add_products_cart_page."""
        add_cart = add_products_cart_page(self.driver)
        add_cart.add_first_product_to_cart().view_cart()
        return self

    def remove_all_products(self):
        """Remove all products from the cart."""
        cart_items = self.driver.find_elements(By.XPATH, "//a[@class='cart_quantity_delete']")
        for item in cart_items:
            item.click()
        empty_msg = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//b[text()='Cart is empty!']"))
        )
        assert empty_msg.is_displayed(), "Cart is not empty after removing products"
        return self
