from selenium.webdriver.common.by import By

from hogwarts.test_selenium.BasePage import BasePage
from hogwarts.test_selenium.ContactPage import Contact_Page

class AddMemberPage(BasePage):

    # def add_menmber(self, name, num, phonenum):
    #
    #     self.driver.find_element(By.CSS_SELECTOR, "#qui_btn.ww_btn.js_add_member").click()
    #     self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys(name)
    #     self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys(num)
    #     self.driver.find_element(By.CSS_SELECTOR, "#qui_inputText.ww_inputText.ww_telInput_mainNumber").send_keys(
    #         phonenum)
    #     self.driver.find_element_by_css_selector("#qui_btn.ww_btn.js_btn_save").click()
    #     return Contact_Page(self.driver)

    _username_locator = (By.ID, "username")
    _acctid_locator = (By.ID, "memberAdd_acctid")

    def goto_contact(self):
        """
        跳转通讯录页面
        :return:
        """

        return Contact_Page(self.driver)

    def add_menmber(self, name, num, phonenum):
        """添加成员操作
        """
        # 填写添加成员信息
        self.find(self._username_locator).send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(num)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phonenum)
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact_Page(self.driver)

    def add_member_fail_by_name(self):
        """ name不填写，一个添加成员的反例操作。
        :return:
        """
        self.find(self._acctid_locator).send_keys("10000")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13188881111")
        # 点击保存
        # self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        error_list = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        # 寻找所有的错误信息，如果不为空，则返回
        error_message = [ele.text for ele in error_list if ele.text != ""]
        return error_message