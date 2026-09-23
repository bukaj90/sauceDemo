from selenium.webdriver.support import expected_conditions as EC
from locators.locators import CheckoutOverviewPageLocator

class CheckoutOverviewPage:
    def __init__(self,driver):
        self.driver = driver

    def get_checkout_product_name(self):
        product_name = self.driver.wait.until(EC.visibility_of_element_located(CheckoutOverviewPageLocator.PRODUCT_NAME))
        return product_name.text

    def get_total(self):
        total_label = self.driver.wait.until(EC.visibility_of_element_located(CheckoutOverviewPageLocator.TOTAL_LABEL))
        return total_label.text

    def finish(self):
        finish_button = self.driver.wait.until(EC.visibility_of_element_located(CheckoutOverviewPageLocator.FINISH_BUTTON))
        finish_button.click()