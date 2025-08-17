import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By

# List all popup/ad selectors
POPUP_SELECTORS = [
    ".popup-class",        # Replace with actual popup class
    ".ad_class_selector",  # Replace with actual ad class
    ".newsletter-popup"    # Example newsletter popup
]
CLOSE_BUTTON_SELECTOR = ".popup-close"  # Replace with actual close button selector

def dismiss_popups(driver):
    """Close or hide any popups/ads on the page."""
    try:
        # Click all close buttons
        close_buttons = driver.find_elements(By.CSS_SELECTOR, CLOSE_BUTTON_SELECTOR)
        for btn in close_buttons:
            try:
                btn.click()
            except:
                pass
        # Hide remaining popups via JS
        driver.execute_script(f"""
        let popups = document.querySelectorAll('{",".join(POPUP_SELECTORS)}');
        popups.forEach(p => p.style.display='none');
        """)
    except:
        pass

def before_all(context):
    browser = context.config.userdata.get("browser", "edge").lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        context.driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.set_preference("privacy.trackingprotection.enabled", True)
        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("media.autoplay.default", 1)
        context.driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")
        context.driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://automationexercise.com/login")

    # Dismiss popups after page load
    dismiss_popups(context.driver)

def after_step(context, step):
    # Dismiss popups every step so they don't block interactions
    dismiss_popups(context.driver)

    if step.status == "failed":
        driver = context.driver
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                driver.page_source,
                name="Page Source",
                attachment_type=allure.attachment_type.HTML
            )
            try:
                logs = driver.get_log("browser")
                allure.attach(str(logs), name="Browser Console Logs",
                              attachment_type=allure.attachment_type.TEXT)
            except Exception:
                pass

def after_all(context):
    if hasattr(context, "driver"):
        context.driver.quit()
