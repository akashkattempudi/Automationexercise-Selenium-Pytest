
from selenium.webdriver.common.by import By

from selenium_tests.test_data import test_data, test_login_data
from selenium.webdriver.remote.webdriver import WebDriver



class register_page:
    def __init__(self, driver: WebDriver):

        self.driver = driver
        self.user = test_data()
        self.users = test_login_data()
        self.data = self.users[0]
    def user_register_data(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Name']").send_keys(self.user["name"])
        self.driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(self.data["email"])
        self.driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
        try:
            message= self.driver.find_element(By.XPATH,"//p[normalize-space()='Email Address already exist!']").text
            assert "exist" in message
            print("Email Address already exist!")
        except Exception as msg:
            print(msg)


