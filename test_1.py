# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_1(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_1(self):
        success = True
        wd = self.wd
        wd.get("https://piexpertonline.power.com/site/login")
        wd.find_element_by_id("username-field").click()
        wd.find_element_by_id("username-field").clear()
        wd.find_element_by_id("username-field").send_keys("pietest0061@piexpert.com")
        wd.find_element_by_id("password-field").click()
        wd.find_element_by_id("password-field").send_keys("\\undefined")
        wd.find_element_by_id("login-submit-btn").click()
        wd.find_element_by_link_text("Component Library").click()
        wd.find_element_by_xpath("//ul[1]/li[2]/span").click()
        wd.find_element_by_id("dlgCompSetOk").click()
        wd.find_element_by_id("closedlgCancel420").click()
        wd.find_element_by_id("logoutLink").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
