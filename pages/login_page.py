from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self,user_name, user_password):
        username_field = self.driver.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys(user_name)

        userpassword_field = self.driver.find_element(By.ID, "password")
        userpassword_field.send_keys(user_password)

        click_button = self.driver.find_element(By.ID, "login-button")
        click_button.click()




