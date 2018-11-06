"""
Example test
"""

import yaml
import unittest
from driver import DriverAbstract
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

with open("./config/config.yml", 'r') as ymlfile:
    main_config = yaml.load(ymlfile)

class TestGoogle(DriverAbstract, unittest.TestCase):

    def test_case_1(self):
        try:
            self.driver.get('https://www.google.com/')
            el = self.driver.find_element_by_class_name('Fx4vi')
            el.click()
            self.driver.get_screenshot_as_file('./screenshots/first.png')
        except NoSuchElementException as ex:
            self.fail(ex.msg)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGoogle)
    unittest.TextTestRunner(verbosity=2).run(suite)
