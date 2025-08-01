# Page Object for Home Page (after login)
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.success_indicator = (By.XPATH, "//a[contains(text(), 'Logout')]")  # Example: Logout link

    def is_logged_in(self):
        return len(self.driver.find_elements(*self.success_indicator)) > 0

