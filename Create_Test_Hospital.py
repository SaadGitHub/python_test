# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re


class CreateTestHospital(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(30)
        self.base_url = "http://leapfrog.survey.dev.lin.panth.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_test_hospital(self):
        driver = self.driver
        driver.get(self.base_url + "/user")
        driver.find_element_by_id("edit-name").clear()
        driver.find_element_by_id("edit-name").send_keys("panth.admin")
        driver.find_element_by_id("edit-pass").clear()
        driver.find_element_by_id("edit-pass").send_keys("@tester26#")
        driver.find_element_by_id("edit-submit").click()
        #wait for Civicrm button
        #EC.presence_of_element_located((By.link_text, "CiviCRM"))
        WebDriverWait(driver, 10).until(EC.title_is, ("CiviCRM"))
        #driver.find_element_by_link_text("CiviCRM").click()
        driver.find_element_by_xpath("//ul[@id='civicrm-menu']/li[4]").click()
        driver.find_element_by_link_text("New Hospital").click()
        driver.find_element_by_id("organization_name").clear()
        driver.find_element_by_id("organization_name").send_keys("Test Hospital 101")
        driver.find_element_by_id("email_1_email").clear()
        driver.find_element_by_id("email_1_email").send_keys("test.hospital.101@gmail.com")
        driver.find_element_by_id("phone_1_phone").clear()
        driver.find_element_by_id("phone_1_phone").send_keys("777-888-5859")
        driver.find_element_by_id("phone_1_phone_ext").clear()
        driver.find_element_by_id("phone_1_phone_ext").send_keys("14152")
        driver.find_element_by_id("website_1_url").clear()
        driver.find_element_by_id("website_1_url").send_keys("http://www.testhospital.com")
        driver.find_element_by_id("address_1_street_address").clear()
        driver.find_element_by_id("address_1_street_address").send_keys("2251 17th Ave")
        driver.find_element_by_id("address_1_city").clear()
        driver.find_element_by_id("address_1_city").send_keys("New York")
        driver.find_element_by_id("address_1_postal_code").clear()
        driver.find_element_by_id("address_1_postal_code").send_keys("11025")
        driver.find_element_by_id("address_1_postal_code_suffix").clear()
        driver.find_element_by_id("address_1_postal_code_suffix").send_keys("21255")
        driver.find_element_by_id("s2id_autogen9").click()
        Select(driver.find_element_by_id("custom_21_-1")).select_by_visible_text("LFG")
        Select(driver.find_element_by_id("custom_23_-1")).select_by_visible_text("Urban")
        Select(driver.find_element_by_id("custom_30_-1")).select_by_visible_text("CAH")
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | id=select2-chosen-17 | ]]
        driver.find_element_by_id("s2id_autogen17_search").send_keys("jax.tester.0@gmail.com")
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | id=select2-result-label-70 | ]]
        driver.find_element_by_id("_qf_Contact_upload_view-bottom").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
