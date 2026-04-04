from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# BasePage class - common reusable methods for all pages
class BasePage:
    # constructor method(runs when an object of the class is created)
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    #  method to click on an element
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    # method to enter text into the input field
    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
    # method to get the text of an element
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    # method to check if an element is visible
    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))