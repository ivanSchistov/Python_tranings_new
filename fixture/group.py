__author__ = 'ichistov'

from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswitch("/group.php") and len(driver.find_elements_by_name("new")) > 0):
           driver.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
        # create new group
        driver.find_element_by_xpath("(//input[@name='new'])[2]").click()
        self.fill_group_form(group)
        driver.find_element_by_name("submit").click()
        self.return_group_page()
        self.group_cahce = None

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        # submit edit group
        driver.find_element_by_name("edit").click()
        # change group name and click update
        self.fill_group_form(new_group_data)
        driver.find_element_by_name("update").click()
        self.return_group_page()
        self.group_cahce = None

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        driver.find_element_by_name("delete").click()
        self.return_group_page()
        self.group_cahce = None

    def return_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements_by_name("selected[]"))

    group_cahce = None

    def get_group_list(self):
        if self.group_cahce is None:
            driver = self.app.driver
            self.open_group_page()
            self.group_cahce = []
            for element in driver.find_elements_by_css_selector("span.group"):
                text = element.get_text()
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cahce.append(Group(name=text, id=id))
        return list(self.group_cahce)
