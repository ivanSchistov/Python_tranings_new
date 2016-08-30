from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from model.contact import Contact
import re

__author__ = 'ichistov'

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswitch("/edit.php") and len(driver.find_elements(By.XPATH,
                ("//input[@value='Enter']")))) > 0:
           driver.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        driver = self.app.driver
        driver.change_field_value("firstname", contact.firstname)
        driver.change_field_value("middlename", contact.middlename)
        driver.change_field_value("lastname", contact.lastname)
        driver.change_field_value("nickname", contact.nickname)
        driver.change_field_value("title", contact.title)
        driver.change_field_value("company", contact.company)
        driver.change_field_value("address", contact.address)
        driver.change_field_value("home", contact.home)
        driver.change_field_value("mobile", contact.mobile)
        driver.change_field_value("email", contact.email)
        driver.change_field_value("homepage", contact.homepage)
        Select(driver.find_element_by_name("bday")).select_by_visible_text("4")
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("April")
        driver.change_field_value("byear", contact.byear)
        driver.change_field_value("work", contact.work)
        driver.change_field_value("fax", contact.fax)
        driver.change_field_value("email2", contact.email2)
        driver.change_field_value("email3", contact.email3)
        Select(driver.find_element_by_name("aday")).select_by_visible_text("5")
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("March")
        driver.change_field_value("ayear", contact.ayear)
        driver.change_field_value("address2", contact.address2)
        driver.change_field_value("phone2", contact.phone2)
        driver.change_field_value("notes", contact.notes)
        driver.find_element(By.XPATH, ("//input[@value='Enter']")).click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index):
        driver = self.app.driver
        self.select_contact_by_index(index)
        # edit first contact
        driver.find_element_by_xpath("//img[@title='Edit']").click()
        # submit editing contact
        driver.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        driver = self.app.driver
        # select first contact
        self.select_contact_by_index(index)
        # submit delete contact
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert().accept()
        self.contact_cache = None

    def return_to_home_page(self):
        self.return_to_home_page()
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.contact_cache = []
            for row in driver.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.app.open_home_page()
        row = driver.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=homephone, mobile=mobilephone,
                       work=workphone, phone2=secondaryphone)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, mobile=mobilephone,
                       work=workphone, phone2=secondaryphone)

