from selenium.webdriver.common.by import By
class LoginPageLocator:
    USER_NAME = (By.ID, "user-name")
    USER_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

class InventoryPageLocator:
    REACT_BURGER_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_SIDEBAR_LINK = (By.ID, "logout_sidebar_link")

class InventoryPageLocator:
    @staticmethod
    def ADD_TO_CART_BUTTON(product_name):
        return (By.XPATH, f"//div[@class='inventory_item'][.//div[text()='{product_name}']]//button")