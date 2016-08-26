from selenium import webdriver
# from __builtin__ import classmethod
import unittest
import time


class lb_modal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "http://legalbarriers.dev.lin2.panth.com/"
        cls.driver.get(cls.base_url)

    def modal_submission(self):
        self.driver.refresh()
        modal_name_xpath = "//input[contains(@id, 'name')]"
        modal_org_xpath = "//input[contains(@id, 'organization')]"
        modal_email_xpath = "//div[contains(@class, 'modal-body')]//input[contains(@id, 'email')]"
        modal_submit_button_xpath = "//input[contains(@id, 'submit_button')]"

        self.driver.find_element_by_xpath(modal_name_xpath).send_keys("Panth Test Name 2")
        self.driver.find_element_by_xpath(modal_org_xpath).send_keys("Panth Test Org 2")
        self.driver.find_element_by_xpath(modal_email_xpath).send_keys("three.testemail@gmail.com")
        self.driver.find_element_by_xpath(modal_submit_button_xpath).click()
        print("submitted")

    def clear_cookie(self):
        time.sleep(3)
        self.driver.delete_all_cookies()
        print
        'cookie cleared'

    # Run all the test cases
    def full_modal(self):
        self.modal_submission()
        self.clear_cookie()

    # loop for x time
    def test_loop(self):
        for _ in range(1, 5):
            self.full_modal()

    @classmethod
    def tearDown(cls):
        # Close the browser window
        cls.driver.quit()
        print
        'should do 2nd'


if __name__ == '__main__':
        unittest.main()