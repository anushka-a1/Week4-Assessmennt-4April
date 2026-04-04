from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# LoginPage class inherits from BasePage, so it can use all common methods like click(), enter_text()
class LoginPage(BasePage):
    # using locators to identify the elements of the login page
    login_link = (By.LINK_TEXT, "Log in")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_button = (By.XPATH, "//input[@value='Log in']")
    #constructor - initializes driver using parent class (BasePage)
    def __init__(self, driver):
        super().__init__(driver)
    # method to click on the login link
    def click_login(self):
        self.click(self.login_link)
    # method to enter email into email field
    def enter_email(self, email):
        self.enter_text(self.email, email)
    # method to enter password into password field
    def enter_password(self, password):
        self.enter_text(self.password, password)
    # method to click login button
    def click_login_button(self):
        self.click(self.login_button)