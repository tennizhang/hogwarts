import time

from appium.webdriver.common.mobileby import MobileBy

from hogwarts.appium.basepage import BasePage


class MemberPage(BasePage):
    def delmember(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/j2z").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        from hogwarts.appium.contactpage import ContactPage
        return ContactPage()

    def delmemberresult(self):
        from hogwarts.appium.contactpage import ContactPage
        delmember_result = ContactPage().numberofnames()
        return delmember_result