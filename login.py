from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")


    # ----------------------LOGIN--------------------

    username_field = driver.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    username_field.send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


    assert "inventory.html" in driver.current_url

    logo = driver.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "app_logo")))
    assert logo.text == 'Swag Labs'

    #--------------------LOGOUT------------------------

    menu_btm = driver.wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    menu_btm.click()

    logout_btm = driver.wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    logout_btm.click()

    login_logo = driver.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_logo")))
    assert login_logo.text == 'Swag Labs'

finally:
    driver.quit()