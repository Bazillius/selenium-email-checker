import time
import yaml
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open("./config/config.yml", 'r') as ymlfile:
    main_config = yaml.load(ymlfile)

driver = webdriver.Chrome(main_config["webdriver_path"])

def login_google():
    is_logged_in = False

    driver.get(main_config["gmail_access"]["host"])

    try:
        time.sleep(1)

        name_box = driver.find_element_by_id('identifierId').send_keys(main_config["gmail_access"]["username"])
        time.sleep(1)

        next_button = driver.find_element_by_id('identifierNext').click()
        time.sleep(1)

        pass_box = driver.find_element_by_name('password').send_keys(main_config["gmail_access"]["password"])
        time.sleep(1)

        next_button = driver.find_element_by_id('passwordNext').click()
        time.sleep(5)

        is_logged_in = True
        driver.get_screenshot_as_file('screen_after_login.png')

    except Exception as ex:
        print(str(ex))
        is_logged_in = False
    finally:
        return is_logged_in

def get_email_title():
    try:
        print('Get title list from last 50 emails...')
        # driver.get('http://gmail.com')
        time.sleep(5)

        # global email_title
        email_title = driver.find_elements_by_xpath("//span[@class='bog']")

        for i in email_title:
            print i.text

    except Exception as ex:
        print(str(ex))
    finally:
        return True


def get_email_time():
    try:
        print('Get time list from last 50 emails...')
        # driver.get('http://gmail.com')
        time.sleep(5)

        # global email_time
        email_time = driver.find_elements_by_xpath("//td[@class='xW xY ']")

        for i in email_time:
            print i.text

    except Exception as ex:
        print(str(ex))
    finally:
        return True


if __name__ == '__main__':
    r_log = login_google()
    if r_log:
        print('Login to gmail...')
        get_email_title()
        get_email_time()
    else:
        print('BooM!!! Something wrong :(')

    if driver is not None:
        driver.quit()

    print('Done')