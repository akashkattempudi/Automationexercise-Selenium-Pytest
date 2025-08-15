# Selenium imports
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import other pages your class interacts with
from selenium_tests.pages.products_page import products_page
class verify_cart_quantity_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def view_product_and_add_quantity(self, quantity):
        products = products_page(self.driver)
        products.verify_home_page()
        products.click_products()
        products.verify_user_navigation()
        products.click_view_product()

        # Update quantity
        qty_input = self.wait.until(EC.visibility_of_element_located((By.ID, "quantity")))
        qty_input.clear()
        qty_input.send_keys(str(quantity))

        # Add to cart
        add_btn = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default cart']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)
        add_btn.click()

        # Go to cart page explicitly
        cart_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/view_cart']")))
        cart_btn.click()
        return self

    def verify_quantity_in_cart(self, expected_qty):
        # Wait for cart quantity to be visible
        qty_display = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//td[@class='cart_quantity']/button"))  # adjust if quantity is in input
        )
        # If it's an input inside the td
        input_elem = qty_display.find_element(By.TAG_NAME, "input")  # or adjust as per actual HTML
        assert input_elem.get_attribute("value") == str(expected_qty), \
            f"Quantity in cart is {input_elem.get_attribute('value')}, expected {expected_qty}"
        return self
