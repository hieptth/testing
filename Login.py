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
from parameterized import parameterized
import readData

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://member.lazada.vn/user/login")

    def tearDown(self):
        self.driver.quit()
    
    @parameterized.expand(readData.readDatafromExcel("Login"))
    def testcase(self,username,password):
        usernameField = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        usernameField.click()
        usernameField.send_keys(username)
        passwordField = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        passwordField.click()
        passwordField.send_keys(password)
        if username == "" or password == "":
            submitField = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
            submitField.click()
        else:
            drag_element = self.driver.find_element(By.XPATH, '//*[@id="nc_2_n1z"]')
            actions = ActionChains(self.driver) 
            actions.drag_and_drop_by_offset(drag_element, 500, 0).perform()
    

if __name__=='__main__':
    unittest.main()