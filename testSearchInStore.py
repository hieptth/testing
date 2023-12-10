from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from readData import readDataFromExcel
from parameterized import parameterized


class SearchInStoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(10)
        self.driver.get("https://www.lazada.vn/shop/phong-vu-official-store/")
        # self.driver.implicitly_wait(10)
        self.driver.set_window_size(1323, 1025)

    def tearDown(self) -> None:
        return self.driver.quit()

    def get_result(self, have_result=True):
        if have_result:
            return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]')
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')

    def get_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="pi-component-container"]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[3]/div/input')

    @parameterized.expand(readDataFromExcel("SearchInStore"))
    def test_search_in_store(self, have_result, query):
        input_search = self.get_input()
        input_search.send_keys(query)
        input_search.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(20)
        if have_result == "yes":
            result = self.get_result()
            print(result.text, " done")
            self.assertNotEqual(result.text, "Search No Result")
        elif have_result == "no":
            result = self.get_result(False)
            self.assertEqual(result.text, "Search No Result")
        else:
            current_url = self.driver.current_url
            self.assertEqual(current_url, 'https://www.lazada.vn/shop/phong-vu-official-store/')


if __name__ == "__main__":
    unittest.main()
