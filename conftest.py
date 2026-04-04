import pytest
from selenium import webdriver
# import your custom class to read data from env.yaml
from config.env import ConfigReader
# pytest fixture (runs before and after each test that uses it)
@pytest.fixture
def setup_and_teardown():
    # read the YAML configuration file using your ConfigReader class
    config = ConfigReader.read_config()
    # access the "qa" environment from the YAML file
    env = config['qa']
    # get the base URL (website link) from the qa environment
    base_url = env['base_url']
    # create a Chrome browser instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    # yield the driver to the test
    # (this pauses here, runs the test, then continues below)
    yield driver
    driver.quit()