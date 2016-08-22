# import credentials as credentials
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest

#test

class Credentials:
    def __init__(self):
        self.admin_email = "leapfrog_admin"
        self.admin_pass = "$uperU$er.leapfrog.16#"



class CreateContents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "http://leapfrog.survey.stg.lin.panth.com/"
        # self.driver.get('http://localhost/drupal7/user')
        cls.credentials = Credentials()

    def test_login(self):
        driver = self.driver
        login_page = "user"
        driver.get(self.base_url + login_page)

        user_name_field = driver.find_element_by_id("edit-name")
        pass_field = driver.find_element_by_id("edit-pass")
        login_button = driver.find_element_by_id("edit-submit")

        # Login process:
        user_name_field.clear()
        user_name_field.send_keys(self.credentials.admin_email)
        pass_field.clear()
        pass_field.send_keys(self.credentials.admin_pass)
        login_button.click()
        # self.driver.implicitly_wait(40)

    def test_verify_login(self):
        driver = self.driver
        try:
            logout_link = driver.find_element_by_xpath(".//*[@id='admin-menu-account']/li[1]/a")
            print logout_link
        except NoSuchElementException:
            print "exception"




        # def tearDown(self):
        #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
