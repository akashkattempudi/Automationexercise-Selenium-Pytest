from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.pages.products_page import products_page
from selenium_tests.pages.login_page_valid import login_page

class search_products_cart_after_login_page:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 1️⃣ Navigate to Products page
    def go_to_products(self):
        products_page(self.driver).click_products()
        return self

    # 2️⃣ Search for a product
    def search_product(self, product_name):
        search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
        search_input.clear()
        search_input.send_keys(product_name)
        self.driver.find_element(By.ID, "submit_search").click()
        return self

    # 3️⃣ Add all visible products to cart
    def add_products_to_cart(self):
        # 1️⃣ Get all Add-to-Cart buttons
        add_btns = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class,'add-to-cart')]"))
        )

        # 2️⃣ Loop through each button
        for btn in add_btns:
            # Scroll button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)

            # Click the button safely
            try:
                if btn.is_displayed() and btn.is_enabled():
                    btn.click()
                else:
                    self.driver.execute_script("arguments[0].click();", btn)
            except:
                # Fallback JS click if normal click fails
                self.driver.execute_script("arguments[0].click();", btn)

            # 3️⃣ Handle modal/pop-up after clicking
            try:
                cont_btn = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue Shopping']"))
                )
                cont_btn.click()
            except:
                # No modal appeared; continue
                pass

        return self

    # 4️⃣ Go to Cart
    def go_to_cart(self):
        cart_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/view_cart']")))
        cart_btn.click()
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'check_out')]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", checkout_btn)
        checkout_btn.click()
        self.driver.find_element(By.XPATH, "//u[normalize-space()='Register / Login']").click()
        return self

    # 5️⃣ Login
    def login(self):
        login = login_page(self.driver)
        login.user_login_data()
        login.click_submit()
        return self

    # 6️⃣ Verify products are still in cart
    def verify_cart_items(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']").click()
        cart_products = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//td[@class='cart_description']/h4/a"))
        )
        assert len(cart_products) > 0, "No products found in cart after login"
        return self

    # Full workflow (optional helper)
