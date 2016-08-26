
from selenium import webdriver
import time
import unittest


class LBTest(unittest.TestCase):
    @classmethod
    def setupclass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "http://legalbarriers.dev.lin2.panth.com/"
        # cls.driver.get(cls.base_url + "user")

        # Defining xpaths
        cls.modal_body_xpath = "//div[contains(@class, 'modal-body')]"
        cls.modal_body_name_xpath = "//input[contains(@id, 'name')][contains(@class, 'form-field')]"
        cls.modal_body_org_xpath = "//input[contains(@id, 'organization')][contains(@class, 'form-field')]"
        cls.modal_body_email_xpath = "//input[contains(@id, 'email')][contains(@class, 'form-field')]"
        cls.modal_body_submit_xpath = "//input[contains(@id, 'submit_button')][contains(@type, 'submit')]"

    # Dara submission
    def data_input(self):
        driver = self.driver
        driver.get(self.base_url)

        modal_body_name_xpath = "//input[contains(@id, 'name')][contains(@class, 'form-field')]"
        modal_body_org_xpath = "//input[contains(@id, 'organization')][contains(@class, 'form-field')]"
        modal_body_email_xpath = "//input[contains(@id, 'email')][contains(@class, 'form-field')]"
        modal_body_submit_xpath = "//input[contains(@id, 'submit_button')][contains(@type, 'submit')]"

        driver.find_element_by_xpath(modal_body_name_xpath).clear()
        driver.find_element_by_xpath(modal_body_name_xpath).send_keys("TestName")
        driver.find_element_by_xpath(modal_body_org_xpath).clear()
        driver.find_element_by_xpath(modal_body_org_xpath).send_keys("TestOrganization")
        driver.find_element_by_xpath(modal_body_email_xpath).clear()
        driver.find_element_by_xpath(modal_body_email_xpath).send_keys("TestEmai@testemail.com")
        driver.find_element_by_xpath(modal_body_submit_xpath).click()
        print("Data Submitted")

    # Deleting browser cookies
    def cookie_delete(self):
        time.sleep(3)
        self.driver.delete_all_cookies()

    # Combining all methods
    def call_all(self):
        self.setupclass()
        self.data_input()

    # Running loop
    def run_loop(self):
        for _ in range(0,20):
            self.call_all()

    # Close the browser window
    @classmethod
    def teardown(cls):
        print("Done")

    if __name__ == '__main__':
        unittest.main()
