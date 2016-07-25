__author__ = 'ichistov'

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_group_page()
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
        self.return_group_page()

    def return_group_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()