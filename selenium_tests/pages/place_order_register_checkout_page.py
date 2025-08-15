# Selenium imports
from selenium.webdriver.remote.webdriver import WebDriver        # type hinting for driver
from selenium.webdriver.common.by import By                       # for locating elements
from selenium.webdriver.support.ui import WebDriverWait           # for explicit waits
from selenium.webdriver.support import expected_conditions as EC   # for EC.element_to_be_clickable and EC.visibility_of_element_located

# Your page objects imports
from selenium_tests.pages.add_products_cart_page import add_products_cart_page
from selenium_tests.pages.register_page_valid import register_page

class place_order_register_checkout_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_and_checkout(self):
        add_cart = add_products_cart_page(self.driver)

        # Add product and handle modal
        add_cart.add_first_product_to_cart().continue_shopping().view_cart()

        # Wait and click checkout safely
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'check_out')]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkout_btn)
        checkout_btn.click()
        self.driver.find_element(By.XPATH, "//u[normalize-space()='Register / Login']").click()
        return self

    def add_product_and_checkout(self):
        add_cart = add_products_cart_page(self.driver)
        add_cart.add_first_product_to_cart().continue_shopping().view_cart()

        # Click checkout
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'check_out')]"))
        )
        checkout_btn.click()

        # Click Register/Login
        register_login_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//u[normalize-space()='Register / Login']"))
        )
        register_login_btn.click()
        return self

    def register_and_place_order(self, payment_data):
        register = register_page(self.driver)
        register.user_register_data()
        register.user_form()
        register.create_account()
        register.click_to_continue()

        # Go back to cart after registration
        self.driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'check_out')]"))
        )
        checkout_btn.click()

        # Proceed with payment
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()
        self.wait.until(EC.visibility_of_element_located((By.NAME, "name_on_card"))).send_keys(payment_data['name'])
        self.driver.find_element(By.NAME, "card_number").send_keys(payment_data['card_number'])
        self.driver.find_element(By.NAME, "cvc").send_keys(payment_data['cvc'])
        self.driver.find_element(By.NAME, "expiry_month").send_keys(payment_data['month'])
        self.driver.find_element(By.NAME, "expiry_year").send_keys(payment_data['year'])
        self.driver.find_element(By.CSS_SELECTOR, "#submit").click()


        success_msg = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[normalize-space()='Congratulations! Your order has been confirmed!']"))
        )
        assert success_msg.is_displayed(), "Order success message not visible"
        return self

