import pytest 
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from parameterized import parameterized
import readData

class AddVoucher(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.lazada.vn")
        self.login("0828696919", "P@ssword123")
        time.sleep(5)
        self.buyProduct()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def login(self, username, password):
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="anonLogin"]/a')
        login_btn.click()

        email_input = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div/div[2]/div/input')
        email_input.send_keys(username)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div/div[3]/div[1]/input')
        password_input.send_keys(password)

        time.sleep(5)

        drag_element = self.driver.find_element(By.XPATH, '//*[@id="nc_2_n1z"]')
        actions = ActionChains(self.driver) 
        actions.drag_and_drop_by_offset(drag_element, 500, 0).perform()
    
    def buyProduct(self):
        product_card = self.driver.find_element(By.XPATH, '//*[@id="J_FlashSale"]/div[2]/div[2]/a[2]')
        product_card.click()

        time.sleep(5)

        buy_btn = self.driver.find_element(By.XPATH, '//*[@id="module_add_to_cart"]/div/button[1]')
        buy_btn.click()

    
    @parameterized.expand(readData.readDataFromExcel("AddVoucher"))
    def testcase(self, Voucher, Output):
        voucher_input = self.driver.find_element(By.XPATH, '//*[@id="automation-voucher-input"]')

        apply_btn = self.driver.find_element(By.XPATH, '//*[@id="automation-voucher-input-button"]')

        voucher_input.send_keys(Voucher)
        apply_btn.click()
        time.sleep(5)

        error_message = self.driver.find_element(By.XPATH, '//*[@id="rightContainer_10010"]/div[3]/div[2]')
        time.sleep(5)
        assert error_message.text == Output


if __name__=='__main__':
    unittest.main()
