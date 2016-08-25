from selenium import webdriver
import unittest


class TestLoginLFS(unittest.TestCase):
    @classmethod
    def setfields(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize.windows()
        cls.base_url = "http://leapfrog.survey.stg.lin.panth.com/"
        cls.driver.get(cls.base_url + "user")

        # Xpaths
        cls.user_name = "//input[contains(@id, 'edit-name')]"
        cls.user_pass = "//input[contains(@id, 'edit-pass')]"
        cls.submut_btn = "//button[contains(@id, 'edit-submit')]"

        # Submission
    def data_submission(self):
        driver = self.driver
        driver = get.(self.base_url + "user")

        driver.find_element_by_xpath("//input[contains(@id, 'edit-name')]").clear()
        driver.find_element_by_xpath("//input[contains(@id, 'edit-name')]").send_keys("leapfrog_admin")
        driver.find_element_by_xpath("//input[contains(@id, 'edit-pass')]").clear()
        driver.find_element_by_xpath("//input[contains(@id, 'edit-pass')]").send_keys("$uperU$er.leapfrog.16#")
        driver.find_element_by_xpath("//button[contains(@id, 'edit-submit')]").click()

    if __name__ == '__main__':
        unittest.main()
