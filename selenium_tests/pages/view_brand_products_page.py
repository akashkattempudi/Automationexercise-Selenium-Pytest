# Selenium imports
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class view_brand_products_page:
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_brand_and_verify(self, brand_xpath, expected_text):
        # Wait until the brand element is visible and clickable
        brand_elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, brand_xpath)))

        # Scroll into view (optional but improves reliability)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", brand_elem)
        brand_elem.click()

        # Verify brand page header is visible
        brand_header = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//h2[contains(text(),'{expected_text}')]"))
        )
        assert brand_header.is_displayed(), f"{expected_text} page not visible"
        return self
