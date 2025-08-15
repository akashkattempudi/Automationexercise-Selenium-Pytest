from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
class products_page:
    def __init__(self,driver: WebDriver):
        self.driver = driver
    def verify_home_page(self):
        assert "Automation" in self.driver.title, "Home page not loaded successfully"
    def click_products(self):
        products_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']"))
        )
        products_button.click()
    def verify_user_navigation(self):
        header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='All Products']"))
        )
        assert header.is_displayed(), "All Products page not visible"
    def verify_products_is_visible(self):
        product_list = self.driver.find_elements(By.XPATH, "//div[@class='features_items']/div")
        assert len(product_list) > 0, "Products list not visible"
        self.driver.execute_script("document.querySelectorAll('iframe').forEach(el => el.style.display = 'none');")
    def click_view_product(self):
        view_product_first = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//a[text()='View Product'])[1]"))
        )
        view_product_first.click()
    def verify_on_product(self):
        product_detail = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-information']"))
        )
        assert product_detail.is_displayed(), "Product detail page not loaded"
    def verify_product_details(self):
        products = [
            self.driver.find_element(By.XPATH, "//div[@class='product-information']/h2").text,  # Name
            self.driver.find_element(By.XPATH, "//div[@class='product-information']/p[1]").text,  # Category
            self.driver.find_element(By.XPATH, "//div[@class='product-information']/span/span").text,  # Price
            self.driver.find_element(By.XPATH, "//div[@class='product-information']/p[2]").text,  # Availability
            self.driver.find_element(By.XPATH, "//div[@class='product-information']/p[3]").text,  # Condition
            self.driver.find_element(By.XPATH, "//div[@class='product-information']/p[4]").text  # Brand
        ]

        labels = ["Name", "Category", "Price"]

        for idx, value in enumerate(products, start=1):
            if idx <= 3:
                print(f"{labels[idx - 1]}: {value}")
            else:
                print(value)

