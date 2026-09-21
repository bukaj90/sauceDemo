import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL, GLOBAL_WAIT, USERS
class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup_saucedemo(self):
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service)
        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(self.driver, GLOBAL_WAIT)
        self.driver.get(BASE_URL)

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

    @pytest.mark.parametrize("user_name, user_password, login_success", [
        (dane["user_name"], dane["user_password"], dane["login_success"]) for dane in USERS.values() #comprehension list
    ], ids=["standard_user_login", "locked_out_user_login"])
    def test_login(self, user_name,user_password, login_success):
        self.login(user_name, user_password)

        if login_success:
            assert "inventory.html" in self.driver.current_url

            logo = self.driver.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "app_logo")))
            assert logo.text == 'Swag Labs'
        else:
            error_msg = self.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
            assert error_msg.text == 'Epic sadface: Sorry, this user has been locked out.'

    @pytest.mark.parametrize("user_name, user_password",[
        (USERS["standard_user_login"]["user_name"],
         USERS["standard_user_login"]["user_password"])
    ])
    def test_logout(self, user_name, user_password):
        self.login(user_name, user_password)
        self.logout()

        login_logo = self.driver.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")))
        assert login_logo.text == 'Swag Labs'