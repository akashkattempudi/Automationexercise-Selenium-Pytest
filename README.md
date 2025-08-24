![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white) 
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white) 
![BDD](https://img.shields.io/badge/BDD-Behave-red?style=for-the-badge&logo=behave&logoColor=white)

Ecommerce-automation-selenium-pytest-bdd

This repository contains an end-to-end Selenium automation framework built using Python, Pytest, Behave (BDD), and the Page Object Model (POM) design pattern. It automates functional testing for the Automation Exercise demo application.

🚀 Features

Selenium WebDriver for browser automation

Pytest for test execution and reporting

Behave for BDD-style test scenarios

Page Object Model (POM) for reusable and maintainable code

HTML and Allure test reports generated automatically

Pytest fixtures and hooks (conftest.py) for setup & teardown

Automated test execution using run_bdd_pytest.bat

📂 Project Structure
Automationexercise-Selenium-Pytest/
│── selenium_tests/
│   ├── pages/        # Page object classes (locators + actions)
│   ├── test_pages/   # Test cases using Pytest
│── features/          # BDD feature files and step definitions (Behave)
│── utilities/         # Helper methods and reusable code
│── reports/           # Generated test reports (HTML & Allure)
│── conftest.py        # Pytest fixtures and browser setup
│── run_bdd_pytest.bat # Batch file to run tests automatically
│── requirements.txt   # Dependencies

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/akashkattempudi/Automationexercise-Selenium-Pytest.git
cd Automationexercise-Selenium-Pytest


Create a virtual environment

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


Run BDD (Behave) tests

behave


Run tests automatically using batch file

run_bdd_pytest.bat


Run a specific Pytest file

pytest selenium_tests/test_pages/test_login.py -v

📊 Reports

HTML report: Detailed browser-based test report in reports/

Allure report: Interactive and visually rich report in reports/allure-results/

Both reports give detailed insights into test execution, failures, and screenshots (if configured).

🛠️ Tech Stack

Language: Python

Automation Tool: Selenium WebDriver

Test Runner: Pytest, Behave (BDD)

Reports: pytest-html, Allure

Design Pattern: Page Object Model (POM)
