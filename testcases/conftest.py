import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        # driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser.................")
    elif browser == 'firefox':
        # driver = webdriver.Firefox()
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching Firefox browser ...................")
    else:
        # driver =webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print("Launching Edge browser ...................")

    return driver

def pytest_addoption(parser): #gets the value from CLI/hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #returns browser value to setup method
    return request.config.getoption("--browser")