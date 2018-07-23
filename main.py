import time
import yaml
import os
import datetime
import mysql.connector
from mysql.connector import errorcode
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

        driver.find_element_by_id('identifierId').send_keys(main_config["gmail_access"]["username"])
        time.sleep(1)

        driver.find_element_by_id('identifierNext').click()
        time.sleep(1)

        driver.find_element_by_name('password').send_keys(main_config["gmail_access"]["password"])
        time.sleep(1)

        driver.find_element_by_id('passwordNext').click()
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
        time.sleep(5)

        global email_title
        email_title = driver.find_elements_by_xpath("//span[@class='bog']")

        # for i in email_title:
            # print i.text

    except Exception as ex:
        print(str(ex))
    finally:
        return True


def get_last_title():

    try:
        db_prod = mysql.connector.connect(host=main_config["db_config"]["prod"]["host"],
                                    user=main_config["db_config"]["prod"]["username"],
                                    passwd=main_config["db_config"]["prod"]["password"],
                                    db=main_config["db_config"]["prod"]["db_name"],
                                    charset='utf8')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    try:
        cursor_prod = db_prod.cursor()

        get_qa_user_id = (main_config["queries"]["get_qa_user_id"])

        cursor_prod.execute(get_qa_user_id)
        user_id = cursor_prod.fetchone()
        # print user_id[0]

        get_qa_last_subject = (main_config["queries"]["get_qa_last_subject"] % user_id[0])

        cursor_prod.execute(get_qa_last_subject)
        global last_subject
        last_subject = cursor_prod.fetchone()
        print "Last subject :", last_subject[0]

        cursor_prod.close()
        db_prod.close()

    except Exception as ex:
        print(str(ex))
    finally:
        return True


def match_title():
    try:
        for i in email_title:
            if last_subject[0] in i.text:
                print "Yes, subject <",last_subject[0],"> found in list"
                driver.find_element_by_xpath("//span [text()='"+last_subject[0]+"']").click()
                driver.get_screenshot_as_file('screen_email.png')
                time.sleep(5)
                email_time = driver.find_elements_by_xpath("//span[@class='g3']")
                for i in email_time:
                    print "Email tame: ", i.text
            else:
                pass
    
    except Exception as ex:
        print(str(ex))
    finally:
        return True



if __name__ == '__main__':
    r_log = login_google()
    if r_log:
        get_email_title()
        get_last_title()
        match_title()
    else:
        print('BooM!!! Something wrong :(')

    if driver is not None:
        driver.quit()

    print('Done')