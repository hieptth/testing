from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from readData import readDataFromExcel
from parameterized import parameterized, parameterized_class

class SignupTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.lazada.vn/")
        self.driver.set_window_size(1323, 1025)
        btn_redirect_signup = self.driver.find_element(By.XPATH, '//*[@id="anonSignup"]/a')
        btn_redirect_signup.click()
        self.driver.implicitly_wait(30)


    def tearDown(self) -> None:
        return self.driver.quit()


    def signup_email(self):
        print("redirect to email sigup")
        btn_email = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[2]/div[5]/div/button')
        btn_email.click()
        self.driver.implicitly_wait(20)


    def get_error(self, typ):
        if typ == "password":
            return self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[1]/div[3]/span')
        elif typ == "account":
            return self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[2]/div[1]/span')
        # return phone or email error element
        return self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[1]/div[1]/span')
    

    def get_input(self, typ):
        if typ == "password":
            return self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[1]/div[3]/input')
        elif typ == "account":
            return self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[2]/div[1]/input')
        # return phone or email error element
        return self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div/div[1]/div[1]/input')


    @parameterized.expand(readDataFromExcel("Signup"))
    def test_sign_up_flows(self, failed_at, phone, email, password, account):
    
        if failed_at == "none" and phone != "":
            input_phone_email = self.get_input("phone")
            input_password = self.get_input("password")
            input_account = self.get_input("account")

            input_phone_email.click()
            input_phone_email.send_keys(phone)
            input_password.send_keys(password)
            input_account.send_keys(account)
            error = self.get_error('phone')
            self.assertEqual(error.text, "")

        elif failed_at == "none" and email != "":
            self.signup_email()
            print('redirected')
            input_phone_email = self.get_input("email")
            input_password = self.get_input("password")
            input_account = self.get_input("account")

            input_phone_email.click()
            input_phone_email.send_keys(email)
            input_password.send_keys(password)
            input_account.send_keys(account)
            error = self.get_error('email')
            self.assertEqual(error.text, "")

        elif failed_at == "phone":
            input_phone_email = self.get_input("phone")
            input_password = self.get_input("password")

            input_phone_email.click()
            input_phone_email.send_keys(phone)
            input_password.click()
            self.driver.implicitly_wait(10)
            error = self.get_error('phone')
            print(error.text, " done")
            self.assertNotEqual(error.text, "")
            
        elif failed_at == "email":
            self.signup_email()
            # enter email
            input_phone_email = self.get_input("email")
            input_password = self.get_input("password")

            input_phone_email.click()
            input_phone_email.send_keys(email)
            self.driver.implicitly_wait(10)
            input_password.click()
            error = self.get_error('email')
            self.assertNotEqual(error.text, "")
        
        elif failed_at == "password":
            input_password = self.get_input("password")
            input_account = self.get_input("account")

            input_password.click()
            input_password.send_keys(password)
            self.driver.implicitly_wait(10)
            input_account.click()
            error = self.get_error('password')
            self.assertNotEqual(error.text, "")

        elif failed_at == "account":
            input_account = self.get_input("account")
            input_password = self.get_input("password")


            input_account.click()
            input_account.send_keys(account)
            self.driver.implicitly_wait(10)
            input_password.click()
            error = self.get_error('account')
            self.assertNotEqual(error.text, "")


if __name__ == "__main__":
    unittest.main()  