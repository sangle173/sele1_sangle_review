from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest

def test_login_success():
    driver = webdriver.Chrome()
    driver.get('http://www.saferailway.somee.com')
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.enter_username('your_username')
    login_page.enter_password('your_password')
    login_page.click_login()

    assert home_page.is_logged_in(), "Login failed!"
    driver.quit()

