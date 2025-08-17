from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium_tests.test_data import test_login_data
class login_page:
    def __init__(self,driver: WebDriver):
        self.driver = driver
    def user_login_data(self):
        users  = test_login_data()
        user = users[1]
        self.driver.find_element(By.CSS_SELECTOR,"input[data-qa='login-email']").send_keys(user['email'])
        self.driver.find_element(By.CSS_SELECTOR,"input[data-qa='login-password']").send_keys(user["password"])
    def click_submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        try:
            message = self.driver.find_element(By.XPATH,  "//p[normalize-space()='Your email or password is incorrect!']").text
            assert "incorrect" in message
            print("❌ Login failed as expected.")
        except Exception as e:
            print("✅ Login successful or unexpected error:", e)


