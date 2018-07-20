import yaml
import os
import datetime
import mysql.connector
from mysql.connector import errorcode
import re

with open("./config/config.yml", 'r') as ymlfile:
    main_config = yaml.load(ymlfile)

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


cursor_prod = db_prod.cursor()

get_qa_user_id = (main_config["queries"]["get_qa_user_id"])

cursor_prod.execute(get_qa_user_id)
user_id = cursor_prod.fetchone()
print user_id

get_qa_last_subject = (main_config["queries"]["get_qa_last_subject"] % user_id)

cursor_prod.execute(get_qa_last_subject)
last_subject = cursor_prod.fetchone()
print last_subject

cursor_prod.close()
db_prod.close()
