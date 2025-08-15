# Selenium imports
from selenium.webdriver.remote.webdriver import WebDriver        # for type hinting 'driver'
from selenium.webdriver.common.by import By                       # for locating elements
from selenium.webdriver.support.ui import WebDriverWait           # for explicit waits
from selenium.webdriver.support import expected_conditions as EC   # for EC.element_to_be_clickable

# Your page objects imports
from selenium_tests.pages.login_page_valid import login_page
from selenium_tests.pages.add_products_cart_page import add_products_cart_page

class place_order_login_before_checkout_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_first_then_checkout(self):
        login = login_page(self.driver)
        login.user_login_data()
        login.click_submit()
        cart_page = add_products_cart_page(self.driver)

        # Add the first product to the cart
        cart_page.add_first_product_to_cart()

        # Click "Continue Shopping"
        cart_page.continue_shopping()

        # View the cart
        cart_page.view_cart()


        return self
