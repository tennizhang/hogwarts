import time

import pytest
from appium.webdriver.common.mobileby import MobileBy
from hogwarts.appium.basepage import BasePage


class ContactPage(BasePage):
    def addmem(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        from hogwarts.appium.addmemberpage import AddMemberPage
        return AddMemberPage()

    def getnumberofname(self):
        # 获取一共有多少个名字
        list = []
        time.sleep(5)
        list = self.driver.find_elements(MobileBy.XPATH, "//*[@text='联系人']/../following-sibling::android.widget.RelativeLayout']")
        return list

    def numberofnames(self):
        numberofnames = len(self.getnumberofname())
        return numberofnames

    def searchmember(self, membername):
        from hogwarts.appium.memberpage import MemberPage
        #点击搜索按钮
        self.driver.find_element(MobileBy.XPATH, "//*[@text='TEST']/../../../following-sibling::android.widget.LinearLayout/*[1]").click()
        #搜索用户
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(membername)
        if '无搜索结果' in self.driver.page_source:
            pytest.xfail(f'无搜索结果{membername}')
            # raise Exception('没有该用户')
        else:
            #删除找到的第一个用户
            self.getnumberofname()[0].click()
        return MemberPage()

