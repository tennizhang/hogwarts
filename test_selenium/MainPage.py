from selenium.webdriver.common.by import By
from selenium import webdriver
from hogwarts.test_selenium.BasePage import BasePage




class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_contact_page(self):
        from hogwarts.test_selenium.ContactPage import Contact_Page
        # self.driver.find_element(By.CSS_SELECTOR, "=#menu_contacts").click()
        return Contact_Page()

    def goto_add_member(self):
        from hogwarts.test_selenium.AddMemberPage import AddMemberPage
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)