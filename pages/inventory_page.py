import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryPageLocator

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Wylogowanie użytkownika")
    def logout(self):
        menu_btm = self.driver.wait.until(EC.visibility_of_element_located(InventoryPageLocator.REACT_BURGER_BTN))
        menu_btm.click()

        logout_btm = self.driver.wait.until(EC.visibility_of_element_located(InventoryPageLocator.LOGOUT_SIDEBAR_LINK))
        logout_btm.click()

    @allure.step("Dodanie produktu do koszyka: {product_name}")
    def add_product_to_cart(self, product_name):
        add_to_cart = self.driver.wait.until(EC.visibility_of_element_located(InventoryPageLocator.ADD_TO_CART_BUTTON(product_name)))
        add_to_cart.click()

    @allure.step("Przejście do koszyka")
    def click_cart(self):
        click_cart = self.driver.wait.until(EC.visibility_of_element_located(InventoryPageLocator.ICON_CART))
        click_cart.click()