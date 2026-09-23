import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import CartPageLocator

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Pobranie nazwy produktu z koszyka")
    def get_product_name(self):
        product_element = self.driver.wait.until(EC.visibility_of_element_located(CartPageLocator.INVENTORY_ITEM_NAME))
        return product_element.text

    @allure.step("Przejście do checkoutu")
    def checkout(self):
        checkout = self.driver.wait.until(EC.visibility_of_element_located(CartPageLocator.BUTTON_CHECKOUT))
        checkout.click()