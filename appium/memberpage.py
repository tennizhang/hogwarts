import time

import pytest
from appium.webdriver.common.mobileby import MobileBy

from hogwarts.appium.basepage import BasePage


class MemberPage(BasePage):
    def delmember(self, membername):
        from hogwarts.appium.contactpage import ContactPage
        self.driver.find_element(MobileBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::android.widget.LinearLayout").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        lists = self.driver.find_element(MobileBy.XPATH, "//*[@ text = '个人信息']/../../../../../following-sibling::android.widget.ScrollView//android.widget.TextView")
        if membername == lists[0].text:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
            return ContactPage()
        else:
            pytest.xfail(f'成员{membername}不匹配')

    def delmemberresult(self):
        from hogwarts.appium.contactpage import ContactPage
        #重新查看名字个数
        delmember_result = ContactPage().numberofnames()
        return delmember_result

