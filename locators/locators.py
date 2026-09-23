from selenium.webdriver.common.by import By
class LoginPageLocator:
    USER_NAME = (By.ID, "user-name")
    USER_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

class InventoryPageLocator:
    REACT_BURGER_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_SIDEBAR_LINK = (By.ID, "logout_sidebar_link")
    ICON_CART = (By.CLASS_NAME, "shopping_cart_link")

    @staticmethod
    def ADD_TO_CART_BUTTON(product_name):
        return (By.XPATH, f"//div[@class='inventory_item'][.//div[text()='{product_name}']]//button")

class CartPageLocator:
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    BUTTON_CHECKOUT = (By.ID, "checkout")

class CheckoutPageLocator:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

class CheckoutOverviewPageLocator:
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    TOTAL_LABEL = (By.CSS_SELECTOR, "[data-test='total-label']")
    FINISH_BUTTON = (By.ID, "finish")

class OrderConfirmationPageLocator:
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    GENERATE_PDF_BUTTON = (By.ID, "generate-pdf-order")