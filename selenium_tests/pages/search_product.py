from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.pages.products_page import products_page

class search_products_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_to_products_page(self):
        products = products_page(self.driver)
        products.verify_home_page()
        products.click_products()
        products.verify_user_navigation()

    def enter_product_name_and_search(self, product_name):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "search_product"))
        )
        search_input.clear()
        search_input.send_keys(product_name)

        search_button = self.driver.find_element(By.ID, "submit_search")
        search_button.click()

    def verify_searched_products_visible(self):
        searched_header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='Searched Products']"))
        )
        assert searched_header.is_displayed(), "'SEARCHED PRODUCTS' section not visible"

    def verify_all_searched_products_are_visible(self):
        # Wait for at least one product name to be present
        searched_products = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='features_items']//div[@class='productinfo text-center']/p")
            )
        )
        assert len(searched_products) > 0, "No searched products are visible"

        # Print all product names
        for idx, product_name in enumerate(searched_products, start=1):
            print(f"{idx}. {product_name.text}")
