from selenium.webdriver.support import expected_conditions as EC
from locators.locators import CheckoutPageLocator

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_form(self,first_name, last_name, zip_code):
        add_first_name = self.driver.wait.until(EC.visibility_of_element_located(CheckoutPageLocator.FIRST_NAME))
        add_first_name.send_keys(first_name)

        add_last_name = self.driver.wait.until(EC.visibility_of_element_located(CheckoutPageLocator.LAST_NAME))
        add_last_name.send_keys(last_name)

        add_zip_code = self.driver.wait.until(EC.visibility_of_element_located(CheckoutPageLocator.ZIP_CODE))
        add_zip_code.send_keys(zip_code)

        continue_button = self.driver.wait.until(EC.visibility_of_element_located(CheckoutPageLocator.CONTINUE_BUTTON))
        continue_button.click()