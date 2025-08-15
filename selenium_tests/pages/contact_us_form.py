import random
import time
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium_tests.test_data import test_data, test_login_data ,contact_us

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Keys


class contact_us_form:
    def __init__(self, driver: WebDriver):

        self.driver = driver
        self.user = test_data()
        self.users = random.choice(test_login_data())
        self.form = contact_us()
    def click_contact_us_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/contact_us']").click()
    def fill_contact_us_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Name']").send_keys(self.user["name"])
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys(self.users["email"])
        self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Subject']").send_keys(self.form["subject"])
        self.driver.find_element(By.CSS_SELECTOR, "#message").send_keys(self.form["message"])
        self.driver.find_element(By.CSS_SELECTOR,"input[name='upload_file']").send_keys(self.form["file"])
    def click_submit_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
        # alert  = self.driver.switch_to.alert
        # alert.accept()
        try:
         message = self.driver.find_element(By.CSS_SELECTOR, ".status.alert.alert-success").text
         assert "submitted" in message
         print("Submitted successfully")
        except Exception as e:
            print(e)

