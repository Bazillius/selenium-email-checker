"""
Google driver
"""
import time
import requests
import unittest
from drivers.AbstractDriver import DriverAbstract
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class TestGoogleMails(DriverAbstract, unittest.TestCase):
    subject = None
    sender = None
    main_config = None
    links = []

    def Auth(self):
        self.driver.get(self.main_config["host"])
        self.driver.find_element_by_id('Email').send_keys(self.main_config["username"])
        self.driver.find_element_by_id('next').click()
        self.driver.find_element_by_id('Passwd').send_keys(self.main_config["password"])
        self.driver.find_element_by_id('signIn').click()

    def test_case_1_login(self):
        try:
            self.Auth()
            self.driver.find_element_by_name('q')
        except NoSuchElementException as ex:
            self.fail(ex)

    def test_case_2_collect_links(self):
        try:
            self.Auth()
            search_query = ""
            if len(self.sender) > 0:
                search_query = "from:{0} ".format(self.sender)

            search_query += "subject:{0}".format(self.subject)
            self.driver.find_element_by_name('q').send_keys(search_query, Keys.ENTER)
            time.sleep(3)
            subjects = self.driver.find_elements_by_xpath("//span[@class='bog']")
            for subject in subjects:
                if len(subject.text) > 0:
                    subject.click()
                    break
            time.sleep(3)
            elements = self.driver.find_element_by_css_selector(".ii.gt").find_elements_by_xpath('.//a')
            for a in elements:
                self.links.append(a.get_attribute("href"))
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_3_check_links(self):
        try:
            for link in self.links:
                print("\n Check status of link: {0}".format(link))
                requests.head(link)
        except Exception as ex:
            self.fail(ex.msg)
