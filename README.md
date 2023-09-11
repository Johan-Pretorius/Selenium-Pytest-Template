# Selenium-Pytest-Template

## About

This testing framework uses the following concepts to ensure a robust and well-suited testing framework:

- **Fixtures**: Reduce coding. [project root]/conftest.py
- **Parameterized data**: Enable easy use case data-driven testing. [project root]/tests/test_[suite].py
- **Configs**: Easily set environmental parameters, i.e., Dev URLs, Ports, and Users, via the command line. [project root]/tests/config.py
- **Page object models**: Make the testing code easier to read and maintain. [project root]/tests/[page_name]_page.py
- **PyTest reporting**: Provide testing proof. Run pytest with `--html=report.html`
- **Improved locators**: Dynamically set the By.[LocatorType]
- **pytest.mark**: Give tests usable metadata for test grouping logic

## Helpful resources

- [Selenium API documentation](https://www.selenium.dev/selenium/docs/api/py/api.html)
- [Selenium window handlers](https://www.selenium.dev/documentation/#moving-between-windows-and-frames)
- [Training page for iFrames](https://techstepacademy.com/iframe-training)
- [LXML documentation](https://lxml.de/)
- [Python VENV documentation](https://docs.python.org/3/library/venv.html)
- [How to send ENTER key to browser](https://stackoverflow.com/questions/1629053/typing-the-enter-return-key-in-selenium)

## Running selectors from the browser's dev tools

Browser Dev Tools Console Commands - Finding Elements

Open your browser dev tools and click on the developer console tab:
- CMD + OPTION + i (Mac)
- CRTL + SHIFT + i (Windows)

Run the following commands for CSS or XPATH element searching:
- Find using an XPATH: $x("//div[@value='note the single quotes']")
- Find using a CSS Selector: $$("div[value='note the single quotes']")

<i>A great XPATH trick is to be able to search for attributes that contain a specific string, see the following example:
- $x("//div[contains(@class, ' event-form__type')]")</i>

A great resource to make element selection easier is to install the [Katalon Rocorder](https://katalon.com/download-recorder) browser plugin to recod the element selectors as you record a browser session.

## Custom common test markers

```config
    webtest: mark a test as a webtest.
    slow: mark test as slow.
    smoke: Minimum tests that must pass post code updates
    regression: Full regression test suite
    system_sample: Tests related to the sample system
    page_training_ground: Tests related to the training_ground page 
    page_login: Tests related to the log in page 
    page_events: Tests related to the events page 
    MQ: Tests that interact with MQ
    user_admin: Tests related to the admin user 
    user_custodian: Tests related to the custodian user
    system_eVoting: Tests related to the eVoting system
    negative_testing: Tests designed to fail
    TC[number]: Test case [number]

```

## Python PIP list

Please find, below, the list of python packages that were used at the time of building this framework:

|Package            |Version |
|-------------------|--------|
|attrs              |23.1.0  |
|certifi            |2023.5.7|
|cffi               |1.15.1  |
|charset-normalizer |3.2.0   |
|colorama           |0.4.6   |
|et-xmlfile         |1.1.0   |
|exceptiongroup     |1.1.2   |
|execnet            |2.0.2   |
|h11                |0.14.0  |
|idna               |3.4     |
|iniconfig          |2.0.0   |
|lxml               |4.9.3   |
|openpyxl           |3.1.2   |
|outcome            |1.2.0   |
|packaging          |23.1    |
|pandas             |2.0.3   |
|paramiko           |3.3.1   |
|pip                |23.1.2  |
|pluggy             |1.2.0   |
|py                 |1.11.0  |
|pycparser          |2.21    |
|PySocks            |1.7.1   |
|pytest             |7.4.0   |
|pytest-html        |3.2.0   |
|pytest-metadata    |3.0.0   |
|pytest-xdist       |3.3.1   |
|requests           |2.31.0  |
|selenium           |4.10.0  |
|setuptools         |65.5.0  |
|sniffio            |1.3.0   |
|sortedcontainers   |2.4.0   |
|trio               |0.22.2  |
|trio-websocket     |0.10.3  |
|urllib3            |2.0.3   |
|wsproto            |1.2.0   |

*It is strongly recommended to create a Python Virtual Environment and get the abovementoned packages installed on this environment.*

### Command to create a new Python virtual environment
```bash
python -m venv /path/to/new/virtual/environment
```

### Command to install the packages when using Umbrella
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pip lxml openpyxl pandas pytest pytest-html pytest-xdist selenium
```

## Python version

python --version:

**Python 3.11.4**

## Sample BAT script to automate running the tests from your desktop

```bash
@echo off
call c:\{pathToYourVenv}\Scripts\activate.bat
timeout /t 1
cd c:\{pathToYourApplication}
timeout /t 1
pytest --html=report.html
timeout /t 1
pause
```
