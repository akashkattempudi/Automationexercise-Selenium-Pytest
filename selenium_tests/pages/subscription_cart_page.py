from selenium_tests.pages.add_products_cart_page import add_products_cart_page
from selenium_tests.pages.subscription_home_page import subscription_home_page

class subscription_cart_page:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cart_with_product(self):
        """Add first product to cart and view cart."""
        add_cart_page = add_products_cart_page(self.driver)
        add_cart_page.add_first_product_to_cart()
        add_cart_page.view_cart()
        return self

    def subscription_steps(self, email):
        """Perform subscription steps from home page."""
        subscription_page = subscription_home_page(self.driver)
        subscription_page.scroll_to_subscription()
        subscription_page.verify_subscription_visible()
        subscription_page.enter_email_and_submit(email)
        subscription_page.verify_success_message()
        return self
