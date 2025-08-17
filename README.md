Automationexercise – Selenium + Pytest + Behave










End-to-end Selenium automation framework using Python, Pytest, Behave (BDD), and POM design pattern for the Automation Exercise demo application.

🚀 Features

Selenium WebDriver for browser automation

Pytest for test execution and reporting

Behave for BDD-style scenarios

Page Object Model (POM) for reusable & maintainable code

HTML and Allure test reports generated automatically

Pytest fixtures & hooks (conftest.py) for setup & teardown

Automated test execution using run_bdd_pytest.bat

📂 Project Structure
<details> <summary>Click to expand</summary>
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

</details>
⚙️ Installation & Setup
<details> <summary>Click to expand</summary>

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

</details>
▶️ Running Tests
<details> <summary>Click to expand</summary>

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

</details>
📊 Reports
<details> <summary>Click to expand</summary>

HTML report: Detailed browser-based test report in reports/

Allure report: Interactive, visually rich report in reports/allure-results/

Both reports provide detailed insights into test execution, failures, and screenshots (if configured).

</details>
✅ Current Status

Selenium + Pytest + Behave framework is fully set up

HTML & Allure reports configured

Tests implemented for login, registration, cart functionality

Utilities and helper methods available

🛠️ Tech Stack

Language: Python

Automation Tool: Selenium WebDriver

Test Runner: Pytest, Behave (BDD)

Reports: pytest-html, Allure

Design Pattern: Page Object Model (POM)

📋 Project Roadmap

Add more test cases (checkout, search, etc.)

Cross-browser testing

Integrate with CI/CD pipelines (GitHub Actions, Jenkins)

Add screenshots for failed tests automatically

Improve test coverage and maintainability

🤝 Contribution Guidelines

Fork the repository

Create a branch for new features/fixes

Follow the POM structure for new tests

Submit a pull request for review
