import logging

from appium.webdriver.common.mobileby import MobileBy

from hogwarts.appium.basepage import BasePage


class AddMemberPage(BasePage):
    def addmember(self, username, phonenumber):
        self.xpathclick("//*[@text='手动输入添加']")
        logging.info(f'点击手动输入添加')
        self.sendkey("//*[contains(@text, '姓名')]/..//android.widget.EditText", username)
        logging.info(f'输入{username}')
        self.sendkey("//*[contains(@text, '手机')]/..//android.widget.EditText", phonenumber)
        logging.info(f'输入{phonenumber}')
        self.xpathclick("//*[@text='保存']")
        logging.info(f'点击保存')
        from hogwarts.appium.contactpage import ContactPage
        return ContactPage(self.driver)

    def addmembersucc(self):
        assert "添加成功" == self.xpath("//*[@class='android.widget.Toast']").get_attribute("text")