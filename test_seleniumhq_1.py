import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

class GetRoot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        # ヘッドレスモードで起動
        options.add_argument('--headless')
        cls.driver = webdriver.Chrome(options=options)
        # Seleniumの公式HPを指定
        cls.base_url = "https://www.selenium.dev/"
        cls.driver.implicitly_wait(30)
        cls.driver.get(cls.base_url)

    def test_get_page(self):
        driver = self.driver
        # HTTPステータスを確認
        r = requests.get(driver.current_url)
        self.assertEqual(r.status_code, 200)
        # ページのタイトルをチェック
        title_target = "Selenium"
        print(driver.title)
        self.assertEqual(title_target, driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()