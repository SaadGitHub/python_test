from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest, time, re
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def login():
    # URL List:

    url = raw_input('Type URL: ')
    username = raw_input('Type username for ' + url + ': ')
    end = username.find('_admin')
    project_name = username[0:end]
    print project_name
    oldpass = "$uperU$er."+project_name+".16#"
    print 'Old Password: '+ oldpass
    newpass = "p@nth#"+project_name+"!$uper"
    print 'New Password: '+ newpass

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url+'user')

    username_field_id = 'edit-name'
    pass_field_id = 'edit-pass'
    login_button_id = 'edit-submit'
    edit_link_xpath = "//a[contains(@href, '/user/1/edit')]"
    edit_page = "/user/1/edit"

    # Edit profile elements:
    current_pass_field_id = "edit-current-pass"
    newpass_field_id = "edit-pass-pass1"
    newpass_conf_field_id = "edit-pass-pass2"

    driver.find_element_by_id(username_field_id).clear()
    driver.find_element_by_id(username_field_id).send_keys(username)
    driver.find_element_by_id(pass_field_id).clear()
    driver.find_element_by_id(pass_field_id).send_keys(oldpass)
    driver.find_element_by_id(login_button_id).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, edit_link_xpath)))
    driver.find_element_by_xpath(edit_link_xpath).click()

    time.sleep(3)
    # driver.get(url+'edit_page')
    

    # Update Password:
    driver.find_element_by_id(current_pass_field_id).clear()
    driver.find_element_by_id(current_pass_field_id).send_keys(oldpass)
    driver.find_element_by_id(newpass_field_id).clear()
    driver.find_element_by_id(newpass_field_id).send_keys(newpass)
    driver.find_element_by_id(newpass_conf_field_id).clear()
    driver.find_element_by_id(newpass_conf_field_id).send_keys(newpass)
    driver.find_element_by_id(login_button_id).click()


    time.sleep(3)


login()
