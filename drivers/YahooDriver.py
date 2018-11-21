"""
Google driver
"""
import time
import unittest
from drivers.AbstractDriver import DriverAbstract
from selenium.common.exceptions import NoSuchElementException


class TestYahooMails(DriverAbstract, unittest.TestCase):
    subject = None
    sender = None
    main_config = None

    def Auth(self):
        self.driver.get(self.main_config["host"])
        self.driver.find_element_by_id('login-username').send_keys(self.main_config["username"])
        self.driver.find_element_by_id('login-signin').click()
        time.sleep(3)
        self.driver.find_element_by_id('login-passwd').send_keys(self.main_config["password"])
        self.driver.find_element_by_id('login-signin').click()
        time.sleep(3)
        #load old version of yahoo
        self.driver.get("https://mail.yahoo.com/neo/b/launch?.src=ym&amp;reason=unsupported_browser")
        time.sleep(3)

    def test_case_1_login(self):
        try:
            self.Auth()

        except NoSuchElementException as ex:
            self.fail(ex)


