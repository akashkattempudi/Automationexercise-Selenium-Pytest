Automationexercise – Selenium + Pytest

This repository contains an end-to-end Selenium automation framework built using Python, Pytest, and the Page Object Model (POM) design pattern. It automates functional testing for the Automation Exercise demo application.

🚀 Features

Selenium WebDriver for browser automation

Pytest for test execution and reporting

Page Object Model (POM) for reusable and maintainable code

HTML and Allure test reports generated automatically

Pytest fixtures and hooks (conftest.py) for setup & teardown

📂 Project Structure
Automationexercise-Selenium-Pytest/
│── selenium_tests/
│   ├── pages/        # Page object classes (locators + actions)
│   ├── test_pages/   # Test cases using Pytest
│── utilities/         # Helper methods and reusable code
│── reports/           # Generated test reports (HTML & Allure)
│── conftest.py        # Pytest fixtures and browser setup
│── requirements.txt   # Dependencies

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/akashkattempudi/Automationexercise-Selenium-Pytest.git
cd Automationexercise-Selenium-Pytest


Create a virtual environment (recommended)

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate


Install dependencies

pip install -r requirements.txt

▶️ Running Tests

Run all tests (HTML report)

pytest -v --html=reports/report_chrome.html --self-contained-html


Run all tests (Allure report)

pytest -v --alluredir=reports/allure-results
allure serve reports/allure-results


Run a specific test file

pytest selenium_tests/test_pages/test_login.py -v

📊 Reports

HTML report: Detailed browser-based test report in reports/

Allure report: Interactive and visually rich report in reports/allure-results/

Both reports give detailed insights into test execution, failures, and screenshots (if configured).

🛠️ Tech Stack

Language: Python

Automation Tool: Selenium WebDriver

Test Runner: Pytest

Reports: pytest-html, Allure

Design Pattern: Page Object Model (POM)
