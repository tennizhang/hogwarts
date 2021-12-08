from appium.webdriver.common.mobileby import MobileBy

from hogwarts.appium.basepage import BasePage


class AddMemberPage(BasePage):
    def addmember(self, username, phonenumber):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//android.widget.EditText").send_keys(username)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//android.widget.EditText").send_keys(phonenumber)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        from hogwarts.appium.contactpage import ContactPage
        return ContactPage()

    def addmembersucc(self):
        assert "添加成功" == self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute("text")