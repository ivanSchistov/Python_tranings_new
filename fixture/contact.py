from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from model.contact import Contact

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

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        driver = self.app.driver
        contacts = []
        for element in driver.find_elements_by_css_selector("span.contact"):
            text = element.get_text()
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text, lastname=text))
        return contacts
