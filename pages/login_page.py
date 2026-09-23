import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LoginPageLocator

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Logowanie użytkownika: {user_name}")
    def login(self, user_name, user_password):
        username_field = self.driver.wait.until(EC.visibility_of_element_located(LoginPageLocator.USER_NAME))
        username_field.send_keys(user_name)

        userpassword_field = self.driver.wait.until(EC.visibility_of_element_located(LoginPageLocator.USER_PASSWORD))
        userpassword_field.send_keys(user_password)

        click_button = self.driver.wait.until(EC.visibility_of_element_located(LoginPageLocator.LOGIN_BUTTON))
        click_button.click()