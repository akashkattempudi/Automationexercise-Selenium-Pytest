# Selenium imports
from selenium.webdriver.remote.webdriver import WebDriver        # for type hinting 'driver'
from selenium.webdriver.common.by import By                       # for locating elements
from selenium.webdriver.support.ui import WebDriverWait           # for explicit waits
from selenium.webdriver.support import expected_conditions as EC   # for EC.element_to_be_clickable

# Your page objects imports
from selenium_tests.pages.register_page_valid import register_page
from selenium_tests.pages.add_products_cart_page import add_products_cart_page

class place_order_register_before_checkout_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register_first_then_checkout(self):
        register = register_page(self.driver)
        register.user_register_data()
        register.user_form()
        register.create_account()
        register.click_to_continue()
        add_cart = add_products_cart_page(self.driver)
        add_cart.add_first_product_to_cart().view_cart()
        checkout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-default check_out']"))
        )
        checkout_btn.click()
        return self