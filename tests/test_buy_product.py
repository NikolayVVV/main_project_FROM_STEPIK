import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options

def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\Professional\\PycharmProjects\\resources\\chromedriver.exe', chrome_options=options)

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    enter_shopping_cart = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id = 'shopping_cart_container']")))
    enter_shopping_cart.click()
    print("Click Enter Shopping Product")

    time.sleep(3)
