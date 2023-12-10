from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from readData import readDataFromExcel
from parameterized import parameterized, parameterized_class

class SearchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.lazada.vn/")
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(1323, 1025)
        
    def tearDown(self) -> None:
        return self.driver.quit()

    def get_result(self, have_result = True):
        if have_result:
            return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
         

    def get_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="q"]')

    @parameterized.expand(readDataFromExcel("Search"))
    def test_search(self, have_result, query):
        input_search = self.get_input()
        input_search.send_keys(query)
        input_search.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(10)
        if have_result == "yes":
            result = self.get_result()
            print(result.text, " done")
            self.assertNotEqual(result.text, "Search No Result")
        elif have_result == "no":
            result = self.get_result(False)
            self.assertEqual(result.text, "Search No Result")
        else:
            current_url = self.driver.current_url
            self.assertEqual(current_url, 'https://www.lazada.vn/')


if __name__ == "__main__":
    unittest.main()