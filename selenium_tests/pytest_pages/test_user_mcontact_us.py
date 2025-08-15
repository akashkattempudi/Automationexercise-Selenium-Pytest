from selenium_tests.pages.contact_us_form import contact_us_form
import time
def test_contact_us(driver):
    contact_us = contact_us_form(driver)
    contact_us.click_contact_us_button()
    contact_us.fill_contact_us_form()
    contact_us.click_submit_button()


