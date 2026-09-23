import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import OrderConfirmationPageLocator

class OrderConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Pobranie komunikatu potwierdzenia zamówienia")
    def get_confirm_order(self):
        confirm_order = self.driver.wait.until(EC.visibility_of_element_located(OrderConfirmationPageLocator.COMPLETE_HEADER))
        return confirm_order.text

    @allure.step("Wygenerowanie PDF zamówienia")
    def generate_pdf(self):
        original_window = self.driver.current_window_handle
        windows_before = self.driver.window_handles

        generate_order_pdf = self.driver.wait.until(EC.visibility_of_element_located(OrderConfirmationPageLocator.GENERATE_PDF_BUTTON))
        generate_order_pdf.click()

        self.driver.wait.until(EC.number_of_windows_to_be(len(windows_before) + 1))

        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

        return self.driver.current_url