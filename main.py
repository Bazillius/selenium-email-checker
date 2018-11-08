"""
Example test
"""
import sys
import unittest
import yaml
from drivers.GoogleDriver import TestGoogleMails
from drivers.YahooDriver import TestYahooMails

with open("./config/config.yml", 'r') as ymlfile:
    main_config = yaml.load(ymlfile)

if __name__ == '__main__':
    subject = sys.argv[1]
    sender = ''
    provider = 'default'
    if len(sys.argv) > 2:
        sender = sys.argv[2]
    if len(sys.argv) > 3:
        sender = sys.argv[3]

    Test = {
        'google': TestGoogleMails,
        'yahoo': TestYahooMails,
        'default': TestGoogleMails
    }[provider]

    Test.subject = subject
    Test.main_config = main_config[provider]
    Test.sender = sender
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
