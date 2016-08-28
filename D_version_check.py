from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import os
import Conf_Reader


class LFS_Drupal_Version_Check(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "http://leapfrog.survey.stg.lin.panth.com/"
        cls.driver.get(cls.base_url + "user")

        # Nesseccary Xpaths
        cls.use_field_xpath = "//input[contains(@class, 'required')][contains(@id, 'edit-name')]"
        cls.pass_field_xpath = "//input[contains(@class, 'required')][contains(@id, 'edit-pass')]"
        cls.login_button_xpath = "//button[contains(@type, 'submit')][contains(@id, 'edit-submit')][contains(@class, 'btn btn-default form-submit')]"
        cls.logut_button_xpath = "//a[contains(@href, '/survey/leapfrog/Logout?return_url=/user/logout')][contains(@title, 'Logout')]"
        cls.admin_menu_report_xpath = "//li[9]/a[contains(@href, '/admin/reports')][contains(text(), 'Reports')]"
        cls.admin_menu_statusreport_xpath = "//li[9]//ul[contains(@class, 'dropdown')]/li/a[contains(@href, '/admin/reports/status')][contains(text(), 'Status report')]"
        cls.drupal_version_verify_xpath = "//tr[contains(@class, 'info')]//td[contains(@class, 'status-value')][contains(text(), '7.43')]"

        # Get the test account credentials from the .credentials file
        credentials_file = os.path.join(os.path.dirname(__file__), 'login.credentials')
        username = Conf_Reader.get_value(credentials_file, 'LOGIN_USER')
        password = Conf_Reader.get_value(credentials_file, 'LOGIN_PASSWORD')
        # cls.username = raw_input('Please type your Username or Email: ')
        # cls.password = raw_input('Please type your password: ')

    # Decleared is_element_present method
    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :param how: By locator type
        :param what: locator value
        """
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    # Admin Login Process
    def admin_login_process(self):
        self.driver.find_element_by_xpath(self.use_field_xpath).clear()
        self.driver.find_element_by_xpath(self.use_field_xpath).send_keys(self.username)
        self.driver.find_element_by_xpath(self.pass_field_xpath).clear()
        self.driver.find_element_by_xpath(self.pass_field_xpath).send_keys(self.password)
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    # Verify User Login
    def login_verify(self):
        self.assertTrue(self.is_element_present(By.XPATH, self.logut_button_xpath))

    # Admin Hover Menu
    def admin_hover_menu(self):
        content_hover_menu = self.driver.find_element_by_xpath(self.admin_menu_report_xpath)
        hover_menu = ActionChains(self.driver).move_to_element(content_hover_menu)
        hover_menu.perform()

        status_report_hover = self.driver.find_element_by_xpath(self.admin_menu_statusreport_xpath)
        hover_status_report_content = ActionChains(self.driver).move_to_element(status_report_hover)
        hover_status_report_content.perform()

    # Access status report page
    def status_report_page(self):
        self.driver.find_element_by_xpath(self.admin_menu_report_xpath).click()
        self.driver.find_element_by_xpath(self.admin_menu_statusreport_xpath).click()
        # verify verison
        self.assertTrue(self.is_element_present(By.XPATH, self.drupal_version_verify_xpath))

    # Run
    def test_runing_script(self):
        self.admin_login_process()
        self.login_verify()
        self.status_report_page()

    @classmethod
    def tearDown(cls):
        # Close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
