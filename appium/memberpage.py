import time

import pytest
from appium.webdriver.common.mobileby import MobileBy

from hogwarts.appium.basepage import BasePage


class MemberPage(BasePage):
    def delmember(self, membername):
        from hogwarts.appium.contactpage import ContactPage
        self.xpathclick("//*[@text='个人信息']/../../../../following-sibling::android.widget.LinearLayout")
        self.xpathclick("//*[@text='编辑成员']").click()
        lists = self.xpath("//*[@ text = '个人信息']/../../../../../following-sibling::android.widget.ScrollView//android.widget.TextView")
        if membername == lists[0].text:
            self.xpathclick("//*[@text='删除成员']")
            self.xpathclick("//*[@text='确定']")
            return ContactPage()
        else:
            pytest.xfail(f'成员{membername}不匹配')

    def delmemberresult(self):
        from hogwarts.appium.contactpage import ContactPage
        #重新查看名字个数
        delmember_result = ContactPage().numberofnames()
        return delmember_result

