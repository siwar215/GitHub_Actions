from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os


class TestTranslatePage(TestCase):
    def setUp(self):
        options = Options()
        options.browser_version = 'latest'
        options.platform_name = 'Windows 11'

        sauce_options = {'username': os.environ['SAUCE_USERNAME'],
                         'browserName': 'Chrome',
                         'build': 'Google translate testing',
                         'name': 'Cloud testing',
                         'accessKey': os.environ['SAUCE_ACCESS_KEY'],
                         'version': '105'}

        options.set_capability('sauce:options', sauce_options)
        sauce_url = os.environ['SAUCE_URL']
        self.driver = webdriver.Remote(command_executor=sauce_url, options=options)
        self.driver.get('https://translate.google.com')

    def test_alert(self):
        self.driver.find_element(By.CLASS_NAME, value="er8xn").send_keys('hello cloud!')

    def tearDown(self):
        self.driver.quit()
