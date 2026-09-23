import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from config import BASE_URL, GLOBAL_WAIT, USERS
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage

class TestAddThing:

    @pytest.fixture(autouse=True)
    def setup_add_thing(self):
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service)
        self.driver.maximize_window()
        self.driver.wait = WebDriverWait(self.driver, GLOBAL_WAIT)
        self.driver.get(BASE_URL)

        login_page = LoginPage(self.driver)
        login_page.login(USERS["standard_user_login"]["user_name"], USERS["standard_user_login"]["user_password"])

        yield
        self.driver.quit()

    def test_add_product_to_cart(self):
        inventory_page = InventoryPage(self.driver)
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.click_cart()

        cart_page = CartPage(self.driver)
        product_name = cart_page.get_product_name()
        assert product_name == 'Sauce Labs Backpack'
        cart_page.checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout_form("Michał", "Tumus", "12-123 Zielonka")

        checkout_overview_page = CheckoutOverviewPage(self.driver)
        check_product_name = checkout_overview_page.get_checkout_product_name()
        assert  check_product_name == 'Sauce Labs Backpack'

        total_price = checkout_overview_page.get_total()
        assert total_price == 'Total: $32.39'

        checkout_overview_page.finish()

        time.sleep(3)