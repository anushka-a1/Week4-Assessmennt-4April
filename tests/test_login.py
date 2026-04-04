# import ConfigReader to read data from env.yaml
from config.env import ConfigReader
from pages.login_page import LoginPage
from utils.loggers import get_logger
# test function for valid login
def test_valid_login(setup_and_teardown):
    # get driver instance from fixture (browser setup)
    driver = setup_and_teardown
    # create object of LoginPage and pass driver
    lp = LoginPage(driver)
    # read configuration data from YAML file
    config = ConfigReader.read_config()
    # access "qa" environment data
    env = config['qa']
    # fetch base URL from config
    BASE_URL = env['base_url']
    # fetch username from config
    USERNAME = env['username']
    # fetch password from config
    PASSWORD = env['password']
    driver.get(BASE_URL)
    get_logger().info("Performing login")
    get_logger().error("Login failed")
    # perform login steps using LoginPage methods
    lp.click_login()
    lp.enter_email(USERNAME)
    lp.enter_password(PASSWORD)
    lp.click_login_button()
    