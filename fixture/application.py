__author__ = 'ichistov'

from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def open_group_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def create_group(self, group):
        driver = self.driver
        # create new group
        driver.find_element_by_xpath("(//input[@name='new'])[2]").click()
        # fill group fields
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.group_name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()

    def return_group_page(self):
        driver = self.driver
        self.return_group_page()
        driver.find_element_by_link_text("group page").click()

    def destroy(self):
        self.driver.quit()

