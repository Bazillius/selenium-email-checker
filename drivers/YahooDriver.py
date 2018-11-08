"""
Example test
"""
import time
import unittest
from drivers.AbstractDriver import DriverAbstract
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class TestYahooMails(DriverAbstract, unittest.TestCase):
    subject = None
    sender = None
    main_config = None
