import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup_saucedemo(self):
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service)
        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.saucedemo.com/")

        yield
        self.driver.quit()

    def login(self, user_name, user_password):
        username_field = self.driver.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys(user_name)

        userpassword_field = self.driver.find_element(By.ID, "password")
        userpassword_field.send_keys(user_password)

        click_button = self.driver.find_element(By.ID, "login-button")
        click_button.click()

    def logout(self):
        menu_btm = self.driver.wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
        menu_btm.click()

        logout_btm = self.driver.wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        logout_btm.click()

    def test_login(self):
        self.login("standard_user", "secret_sauce")

        assert "inventory.html" in self.driver.current_url

        logo = self.driver.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "app_logo")))
        assert logo.text == 'Swag Labs'

    def test_logout(self):
        self.login("standard_user", "secret_sauce")
        self.logout()

        login_logo = self.driver.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")))
        assert login_logo.text == 'Swag Labs'