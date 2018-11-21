"""
DriverAbstract class
"""

from selenium import webdriver


class DriverAbstract:
    driver = None

    def setUp(self):

        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()



