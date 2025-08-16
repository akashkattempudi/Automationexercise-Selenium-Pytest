import pytest
import allure
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge",
        help="Browser to run tests: chrome, firefox, edge"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        options = ChromeOptions()
        options.page_load_strategy = 'eager'

        # Disable notifications and pop-ups
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")  # disables ad-related extensions
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.page_load_strategy = 'eager'

        # Tracking protection
        options.set_preference("privacy.trackingprotection.enabled", True)
        options.set_preference("privacy.trackingprotection.pbmode.enabled", True)
        options.set_preference("privacy.trackingprotection.fingerprinting.enabled", True)
        options.set_preference("privacy.trackingprotection.cryptomining.enabled", True)

        # Disable pop-ups, notifications, and autoplay
        options.set_preference("dom.disable_open_during_load", True)
        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("media.autoplay.default", 1)

        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.page_load_strategy = 'eager'

        # Disable notifications and pop-ups
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get("https://automationexercise.com/login")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def pytest_configure(config):

    if config.getoption('--html'):
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_file = config.getoption('--html')
        # Add timestamp before file extension
        if report_file.endswith(".html"):
            report_file = report_file.replace(".html", f"_{now}.html")
        else:
            report_file = f"{report_file}_{now}.html"
        config.option.htmlpath = report_file


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
