from selenium.webdriver.common.by import By

from hogwarts.test_selenium.BasePage import BasePage


class Contact_Page(BasePage):

    def check_member(self):
        from hogwarts.test_selenium.AddMemberPage import AddMemberPage
        return ['abc']
