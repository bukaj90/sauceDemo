from selenium.webdriver.support import expected_conditions as EC
from locators.locators import OrderConfirmationPageLocator

class OrderConfirmationPage:
    def __init__(self,driver):
        self.driver = driver

    def get_confirm_order(self):
        confirm_order = self.driver.wait.until(EC.visibility_of_element_located(OrderConfirmationPageLocator.COMPLETE_HEADER))
        return  confirm_order.text

    def generate_pdf(self):
        generate_order_pdf = self.driver.wait.until(EC.visibility_of_element_located(OrderConfirmationPageLocator.GENERATE_PDF_BUTTON))
        generate_order_pdf.click()