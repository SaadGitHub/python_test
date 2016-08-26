from selenium import webdriver
import unittest


class TestLoginLFS(unittest.TestCase):
    @classmethod
    def setfields(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "http://leapfrog.survey.stg.lin.panth.com/"
        cls.driver.get(cls.base_url)




        # Submission
    def data_submission(self):
        self.driver.refresh()
        driver = self.driver
        driver.get(self.base_url + "user")

        # Xpaths
        user_name = "//input[contains(@id, 'edit-name')]"
        user_pass = "//input[contains(@id, 'edit-pass')]"
        submit_btn = "//button[contains(@id, 'edit-submit')]"

        driver.find_element_by_xpath(user_name).clear()
        driver.find_element_by_xpath(user_name).send_keys("leapfrog_admin")
        driver.find_element_by_xpath(user_pass).clear()
        driver.find_element_by_xpath(user_pass).send_keys("$uperU$er.leapfrog.16#")
        driver.find_element_by_xpath(submit_btn).click()

    # @classmethod
    # def tearDown(cls):
    #     # Close the browser window
    #     # cls.driver.quit()

if __name__ == '__main__':
    unittest.main()