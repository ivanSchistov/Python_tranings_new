from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

__author__ = 'ichistov'

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.home)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(contact.homepage)
        Select(driver.find_element_by_name("bday")).select_by_visible_text("4")
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("April")
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(contact.byear)
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.work)
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax)
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(contact.email2)
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(contact.email3)
        Select(driver.find_element_by_name("aday")).select_by_visible_text("5")
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("March")
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(contact.ayear)
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(contact.address2)
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(contact.phone2)
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(contact.notes)
        driver.find_element(By.XPATH, ("//input[@value='Enter']")).click()

    def modify_first_contact(self):
        driver = self.app.driver
        # edit first contact
        driver.find_element_by_xpath("//img[@title='Edit']").click()
        # submit editing contact
        driver.find_element_by_name("update").click()


    def delete_first_contact(self):
        driver = self.app.driver
        # select first contact
        driver.find_element_by_name("selected[]").click()
        # submit delete contact
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert().accept()

    def return_to_home_page(self):
        self.return_to_home_page()
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()