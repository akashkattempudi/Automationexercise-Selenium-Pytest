import random
import time
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium_tests.test_data import test_data
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Keys
class register_page:
    def __init__(self,driver: WebDriver):
        self.driver = driver
        self.user = test_data()
    def user_register_data(self):
        self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Name']").send_keys(self.user["name"])
        self.driver.find_element(By.CSS_SELECTOR,"input[data-qa='signup-email']").send_keys(f"{self.user["email"]}{random.randint(1,99999)}@gmail.com")
        self.driver.find_element(By.CSS_SELECTOR,"button[data-qa='signup-button']").click()
        
    def user_form(self):

        self.driver.find_element(By.CSS_SELECTOR,"#id_gender1").click()
        self.driver.find_element(By.CSS_SELECTOR,"#id_gender2").click()
        self.driver.find_element(By.CSS_SELECTOR,"#id_gender1").click()
        self.driver.find_element(By.CSS_SELECTOR,"#password").send_keys(self.user["password"])
        date_select = Select(self.driver.find_element(By.CSS_SELECTOR,"#days"))
        date_select.select_by_visible_text(self.user["day"])
        month_select = Select(self.driver.find_element(By.CSS_SELECTOR,"#months"))
        month_select.select_by_visible_text(self.user["month"])
        year_select = Select(self.driver.find_element(By.CSS_SELECTOR,"#years"))
        year_select.select_by_visible_text(self.user["year"])
        self.driver.find_element(By.CSS_SELECTOR,"#newsletter").click()
        self.driver.find_element(By.CSS_SELECTOR,"#newsletter").click()
        self.driver.find_element(By.CSS_SELECTOR,"#optin").click()
        self.driver.find_element(By.CSS_SELECTOR,"#optin").click()
        self.driver.find_element(By.CSS_SELECTOR,"#first_name").send_keys(self.user["first_name"])
        self.driver.find_element(By.CSS_SELECTOR,"#last_name").send_keys(self.user["last_name"])
        self.driver.find_element(By.CSS_SELECTOR,"#company").send_keys(self.user["company"])
        self.driver.find_element(By.CSS_SELECTOR,"#address1").send_keys(self.user["address1"])
        self.driver.find_element(By.CSS_SELECTOR,"#address2").send_keys(self.user["address2"])
        country_select = Select(self.driver.find_element(By.CSS_SELECTOR,"#country"))
        country_select.select_by_visible_text(self.user["country"])
        self.driver.find_element(By.CSS_SELECTOR,"#state").send_keys(self.user["state"])
        self.driver.find_element(By.CSS_SELECTOR,"#city").send_keys(self.user["city"])
        self.driver.find_element(By.CSS_SELECTOR,"#zipcode").send_keys(self.user["zipcode"])
        self.driver.find_element(By.CSS_SELECTOR,"#mobile_number").send_keys(self.user["mobile"])
    def create_account(self):
        self.driver.find_element(By.CSS_SELECTOR,"button[data-qa='create-account']").click()
    def click_to_continue(self):
        self.driver.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()
