import undetected_chromedriver as uc
import pytest 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import platform 
import time 


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = uc.Chrome()
        print("Launching Chrome Browser......")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser......")
    else:
        driver = uc.Chrome()
    
    wait = WebDriverWait(driver, 50)
    yield driver, wait  # Provides driver and wait to the test function and pauses until test completion
    driver.quit()  
    time.sleep(5)

def pytest_addoption(parser): # This will get the value from CLI / hooks
    parser.addoption("--browser") 

@pytest.fixture
def browser(request): # This will return the Browser value to setup method
    return request.config.getoption('--browser')


################ Pytest HTML Report ###################
# It is hook for adding environment info to HTML Report
def pytest_configure(config):
    config.option.htmlpath = "Reports/report.html"
    config.stash[metadata_key]['Project Name'] = 'nop Commerce'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['Tester'] = 'Aniket'
    config.stash[metadata_key]['OS'] = platform.system()  # Get the OS name
    config.stash[metadata_key].pop('JAVA_HOME')
    config.stash[metadata_key].pop('Plugins')
