from selenium.webdriver.remote.webdriver import WebDriver
from selenium_tests.pages.login_page_valid import login_page
from selenium.webdriver.common.by import By


class logout_page:
    def __init__(self,driver: WebDriver):
        self.driver  = driver
    def login_user_page(self):
        logout = login_page(self.driver)
        logout.user_login_data()
        logout.click_submit()
        return self
    def logout_user_page(self):
        self.driver.find_element(By.CSS_SELECTOR,"a[href='/logout']").click()
        return self



