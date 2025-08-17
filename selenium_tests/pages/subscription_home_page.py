import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class subscription_home_page:
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def scroll_to_subscription(self):
        subscription = self.wait.until(
            EC.presence_of_element_located((By.ID, "susbscribe_email"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", subscription)
        time.sleep(0.5)
        return self

    def verify_subscription_visible(self):
        heading = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Subscription']"))
        )
        assert heading.is_displayed(), "Subscription heading not visible"
        return self

    def enter_email_and_submit(self, email):
        email_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, "susbscribe_email"))
        )
        email_input.clear()
        email_input.send_keys(email)
        self.driver.find_element(By.ID, "subscribe").click()
        return self

    def verify_success_message(self):
        success = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'You have been successfully subscribed!')]")
            )
        )
        assert success.is_displayed(), "Subscription success message not visible"
        return self
