# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


def is_alert_present(self):
    try:
        self.driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True


class AddNewGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_new_group(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("groups").click()
        driver.find_element_by_xpath("(//input[@name='new'])[2]").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("test_group")
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("qwerty")
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("qwerty")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("group page").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
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
