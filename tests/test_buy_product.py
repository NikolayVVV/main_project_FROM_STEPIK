import time
from lib2to3.pgen2 import driver

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options

from pages.main_page import Main_page
from pages.payment_page import Payment_page


# @pytest.mark.run(order=3)
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='D:\\pythonProjectTest\\chromedriver.exe', chrome_options=options)

    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    print("Finish Test 1")
    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

    # time.sleep(3)

#
# @pytest.mark.run(order=1)
def test_buy_product_2(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='D:\\pythonProjectTest\\chromedriver.exe', chrome_options=options)

    print("Start Test 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    print("Finish Test 2")
#
#
# @pytest.mark.run(order=2)
def test_buy_product_3(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(
        executable_path='D:\\pythonProjectTest\\chromedriver.exe', chrome_options=options)

    print("Start Test 3")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    print("Finish Test 3")
