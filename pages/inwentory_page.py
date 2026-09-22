from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

    def logout(self):
        menu_btm = self.driver.wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
        menu_btm.click()

        logout_btm = self.driver.wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        logout_btm.click()
