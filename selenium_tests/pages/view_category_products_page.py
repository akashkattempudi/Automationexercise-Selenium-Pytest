from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class view_category_products_page:
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_category_and_verify(self, category_xpath, expected_text):
        # Wait until category element is clickable
        category_elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, category_xpath)))

        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", category_elem)
        category_elem.click()

        # Verify category page header is visible
        cat_header = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//h2[contains(text(),'{expected_text}')]"))
        )
        assert cat_header.is_displayed(), f"{expected_text} page not visible"
        return self
