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

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://member.lazada.vn/user/login")

    def tearDown(self):
        self.driver.quit()
    
    @parameterized.expand(readData.readDatafromExcel("TrackingOrder"))
    def testcase(self,orderId):
        #Change language of lazada
        languageFields = self.driver.find_elements(By.XPATH, "//span[text()='change language']")
        if len(languageFields) != 0:
            languageField = languageFields[0]
            WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable(self.driver.find_element(By.XPATH, "//span[text()='change language']")))
            languageField.click()
            enIcon = self.driver.find_element(By.CLASS_NAME,"lzd-switch-icon-en")
            WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable(self.driver.find_element(By.CLASS_NAME,"lzd-switch-icon-en")))
            enIcon.click()
            time.sleep(5)

        #Fill user name and password
        usernameField = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        usernameField.click()
        usernameField.send_keys("thuctanphu12@gmail.com")
        passwordField = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        passwordField.click()
        passwordField.send_keys("Hatemyself@1001@@")
        time.sleep(5)
        drag_element = self.driver.find_element(By.XPATH, '//*[@id="nc_2_n1z"]')
        actions = ActionChains(self.driver) 
        actions.drag_and_drop_by_offset(drag_element, 500, 0).perform()
        time.sleep(5)

        #Fill OrderID
        trackingOrderField = self.driver.find_element(By.XPATH, "//span[text()='Track my order']")
        trackingOrderField.click()
        inputField = self.driver.find_element(By.ID,"topActionTrackOrderNumber")
        inputField.send_keys(orderId)
        inputField.send_keys(Keys.ENTER)    

if __name__=='__main__':
    unittest.main()