@echo off
setlocal

:: Auto-detect venv
if exist ".venv\Scripts\activate.bat" (
    set VENV_DIR=.venv\Scripts
) else if exist "venv\Scripts\activate.bat" (
    set VENV_DIR=venv\Scripts
) else (
    echo ❌ No virtual environment found. Please create one.
    exit /b 1
)

:: Ask user for browser input
set /p BROWSER=Enter browser (chrome/firefox/edge) [default=edge]:
if "%BROWSER%"=="" set BROWSER=edge

:: Create reports folder if not exists
if not exist reports mkdir reports

:: Create timestamp (simple version, may vary by locale)
set DATESTAMP=%date:~-4%-%date:~7,2%-%date:~4,2%_%time:~0,2%-%time:~6,2%
set DATESTAMP=%DATESTAMP: =0%

:: Display menu
echo.
echo Select test to run:
echo   1 = Behave only
echo   2 = Pytest only
echo   3 = Both Behave and Pytest
set /p CHOICE=Enter choice [1-3]:

:: Run Behave if choice 1 or 3
if "%CHOICE%"=="1" (
    echo === Running Behave tests with HTML Report on %BROWSER% ===
    %VENV_DIR%\behave -D browser=%BROWSER% -f behave_html_formatter:HTMLFormatter -o reports\behave_report_%DATESTAMP%.html
    echo ✅ Behave report generated -> reports\behave_report_%DATESTAMP%.html
)

if "%CHOICE%"=="3" (
    echo === Running Behave tests with HTML Report on %BROWSER% ===
    %VENV_DIR%\behave -D browser=%BROWSER% -f behave_html_formatter:HTMLFormatter -o reports\behave_report_%DATESTAMP%.html
    echo ✅ Behave report generated -> reports\behave_report_%DATESTAMP%.html
)

:: Run Pytest if choice 2 or 3
if "%CHOICE%"=="2" (
    echo === Running Pytest tests with Allure Results on %BROWSER% ===
    set ALLURE_RESULTS=reports\allure-results-%DATESTAMP%
    set ALLURE_REPORT=reports\allure-report-%DATESTAMP%
    %VENV_DIR%\pytest --browser=%BROWSER% --alluredir=%ALLURE_RESULTS% -q
    echo === Generating Allure Static Report ===
    allure generate %ALLURE_RESULTS% -o %ALLURE_REPORT% --clean
    echo === Opening Allure Report ===
    start %ALLURE_REPORT%\index.html
    echo ✅ Allure report generated -> %ALLURE_REPORT%\index.html
)

if "%CHOICE%"=="3" (
    echo === Running Pytest tests with Allure Results on %BROWSER% ===
    set ALLURE_RESULTS=reports\allure-results-%DATESTAMP%
    set ALLURE_REPORT=reports\allure-report-%DATESTAMP%
    %VENV_DIR%\pytest --browser=%BROWSER% --alluredir=%ALLURE_RESULTS% -q
    echo === Generating Allure Static Report ===
    allure generate %ALLURE_RESULTS% -o %ALLURE_REPORT% --clean
    echo === Opening Allure Report ===
    start %ALLURE_REPORT%\index.html
    echo ✅ Allure report generated -> %ALLURE_REPORT%\index.html
)

endlocal
pause
