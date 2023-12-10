import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from parameterized import parameterized
import readData

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://member.lazada.vn/user/login")

    def tearDown(self):
        self.driver.quit()
    
    @parameterized.expand(readData.readDataFromExcel("Login"))
    def testcase(self,username,password,expected):
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

        #Input the username, password and assert
        usernameField = self.driver.find_element(By.XPATH, '//input[@type="text"]')
        usernameField.click()
        usernameField.send_keys(username)
        passwordField = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        passwordField.click()
        passwordField.send_keys(password)
        time.sleep(5)
        if username == "":
            submitField = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
            submitField.click()
            userErrMsg = self.driver.find_elements(By.XPATH, '//input[@error="You can\'t leave this empty"]')
            assert len(userErrMsg) != 0
        elif password == "":
                drag_element = self.driver.find_element(By.XPATH, '//*[@id="nc_2_n1z"]')
                actions = ActionChains(self.driver) 
                actions.drag_and_drop_by_offset(drag_element, 500, 0).perform()
                passwordErrMsg = self.driver.find_elements(By.XPATH, '//input[@error="You can\'t leave this empty"]')
                assert len(passwordErrMsg) != 0
        else:
            drag_element = self.driver.find_element(By.XPATH, '//*[@id="nc_2_n1z"]')
            actions = ActionChains(self.driver) 
            actions.drag_and_drop_by_offset(drag_element, 500, 0).perform()
            if expected != "": 
                errorMsg = self.driver.find_element(By.CLASS_NAME, 'next-feedback-content')
                assert expected == errorMsg.text

if __name__=='__main__':
    unittest.main()