from selenium.webdriver.support import expected_conditions as EC
from locators.locators import OrderConfirmationPageLocator

class OrderConfirmationPage:
    def __init__(self,driver):
        self.driver = driver

    def get_confirm_order(self):
        confirm_order = self.driver.wait.until(EC.visibility_of_element_located(OrderConfirmationPageLocator.COMPLETE_HEADER))
        return  confirm_order.text

    def generate_pdf(self):
        original_window = self.driver.current_window_handle # zapisanie identyfikatora aktualnej karty (na której jestem )
        windows_before = self.driver.window_handles  #zapisanie wszystkich otwartych kart

        generate_order_pdf = self.driver.wait.until(EC.visibility_of_element_located(OrderConfirmationPageLocator.GENERATE_PDF_BUTTON))
        generate_order_pdf.click()

        self.driver.wait.until(EC.number_of_windows_to_be(len(windows_before) + 1)) # explicit wait czeka aż liczba kart wzrosnie o 1

        new_window = [window for window in self.driver.window_handles if window != original_window][0] # przejsćie przez wszystkie otwarte karty  i wybrania tej ktora nie jest oryginalna
        self.driver.switch_to.window(new_window) # skupienie na nowej karcie

        return self.driver.current_url