from selenium_tests.pages.subscription_cart_page import subscription_cart_page

def test_subscription_cart_page(driver):
    sub_cart = subscription_cart_page(driver)
    sub_cart.go_to_cart_with_product()
    sub_cart.subscription_steps("cart@example.com")
