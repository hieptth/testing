from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from readData import readDataFromExcel
from parameterized import parameterized, parameterized_class

class SignupTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.lazada.vn/")

    def tearDown(self) -> None:
        return self.driver.close()

    

if __name__ == "__main__":
    unittest.main()
    