import os

import pytest
from selenium import webdriver

driver = None    #declare driver as global variable for get_screenshot() method


#mandatory step -- registration of options before using/sending from terminal
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
#--browser_name = same as line 14; default="chrome" -> if no browser identified from user's input, then the test will run in chrome by default
#cmd pattern  in terminal =  NEW PATH>py.test filename.py --browser_name
#final cmd =  dentsu\Documents\Python_Course_udemy\SampleProjectPytest>py.test test_SampleProjecte2e.py --browser_name edge ---> here, this entire path is coming as a request

# In above final cmd: configuration option = --browser_name edge (i.e anything written after filename.py)
#Hence, (--browser_name) is the option &&& (edge) is the value of the option

#NOTE: here, we are externally (from terminal) asking the pytest to run code in edge without touching the code


@pytest.fixture(scope="function")
def browserInstance(request):  #'request' has access to the cmd that is being sent from terminal
                               #'request' is default globally available for every fixture in pytest

    global driver     #this global driver is picked from line-4
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()   # Prerequisite = initializing/activating driver in case of chrome
        driver.implicitly_wait(5)  # Prerequisite
        driver.maximize_window()

    elif browser_name == "edge":
        driver = webdriver.Edge()  # Prerequisite = initializing driver in case of edge
        driver.implicitly_wait(5)     # Prerequisite
        driver.maximize_window()

    yield driver                  # Once the prerequisite code is executed, the 'driver' is returned
    driver.close()                 # this 'driver' is sent/returned to test_SampleProjecte2e.py file


#Capture screenshots and attach to HTML report for the failed tests automatically:
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    pytest_html = item.config.pluginmanager.getplugin('html')

    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:

        reports_dir = os.path.join(os.path.dirname(__file__), "reports")

        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)

        file_name = os.path.join(
            reports_dir,
            report.nodeid.replace("::", "_") + ".png"
        )

        print("file name is " + file_name)

        _capture_screenshot(file_name)

        if os.path.exists(file_name):
            html = '<div><img src="{}" alt="screenshot" style="width:600px;height:300px;" onclick="window.open(this.src)"/></div>'.format(file_name)
            extra.append(pytest_html.extras.html(html))

    report.extra = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)     #using the activated global driver

