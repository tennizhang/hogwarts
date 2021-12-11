from appium.webdriver.common.mobileby import MobileBy

from hogwarts.appium.basepage import BasePage


class AddMemberPage(BasePage):
    def addmember(self, username, phonenumber):
        self.xpathclick("//*[@text='手动输入添加']")
        self.sendkey("//*[contains(@text, '姓名')]/..//android.widget.EditText", username)
        self.sendkey("//*[contains(@text, '手机')]/..//android.widget.EditText", phonenumber)
        self.xpathclick("//*[@text='保存']")
        from hogwarts.appium.contactpage import ContactPage
        return ContactPage()

    def addmembersucc(self):
        assert "添加成功" == self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute("text")