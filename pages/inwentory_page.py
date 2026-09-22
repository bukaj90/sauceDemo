from selenium.webdriver.support import expected_conditions as EC
from locators.locators import InventoryPageLocator
class InventoryPage:

    def __init__(self,driver):
        self.driver = driver

    def logout(self):
        menu_btm = self.driver.wait.until(EC.visibility_of_element_located(InventoryPageLocator.REACT_BURGER_BTN))
        menu_btm.click()

        logout_btm = self.driver.wait.until(EC.visibility_of_element_located(InventoryPageLocator.LOGOUT_SIDEBAR_LINK))
        logout_btm.click()