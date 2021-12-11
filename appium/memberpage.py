import time

from appium.webdriver.common.mobileby import MobileBy

from hogwarts.appium.basepage import BasePage


class MemberPage(BasePage):
    def delmember(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::android.widget.LinearLayout").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        from hogwarts.appium.contactpage import ContactPage
        return ContactPage()

    def delmemberresult(self):
        from hogwarts.appium.contactpage import ContactPage
        #重新查看名字个数
        delmember_result = ContactPage().numberofnames()
        return delmember_result

