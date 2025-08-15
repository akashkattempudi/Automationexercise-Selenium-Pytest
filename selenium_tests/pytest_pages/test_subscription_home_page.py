from selenium_tests.pages.subscription_home_page import subscription_home_page
from selenium_tests.pages.verify_cart_quantity_page import verify_cart_quantity_page

def test_subscription_home_page(driver):
    subscription_page = subscription_home_page(driver)

    # Scroll to subscription section
    subscription_page.scroll_to_subscription()

    # Verify subscription heading is visible
    subscription_page.verify_subscription_visible()


    subscription_page.enter_email_and_submit("home@example.com")

    subscription_page.verify_success_message()
