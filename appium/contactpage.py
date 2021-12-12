import time

import pytest
from appium.webdriver.common.mobileby import MobileBy
from hogwarts.appium.basepage import BasePage


class ContactPage(BasePage):
    def addmem(self):
        self.xpathclick("//*[@text='添加成员']")
        from hogwarts.appium.addmemberpage import AddMemberPage
        return AddMemberPage(self.driver)

    def getnumberofname(self):
        #获取名字的列表
        list = []
        time.sleep(5)
        list = self.xpath("//*[@text='联系人']/../following-sibling::android.widget.RelativeLayout']")
        return list

    def numberofnames(self):
        # 获取一共有多少个名字
        numberofnames = len(self.getnumberofname())
        return numberofnames

    def searchmember(self, membername):
        from hogwarts.appium.memberpage import MemberPage
        #点击搜索按钮
        self.xpathclick("//*[@text='TEST']/../../../following-sibling::android.widget.LinearLayout/*[1]")
        #搜索用户
        self.sendkey("//*[@text='搜索']", membername)
        if '无搜索结果' in self.driver.page_source:
            pytest.xfail(f'无搜索结果{membername}')
            # raise Exception('没有该用户')
        else:
            #删除找到的第一个用户
            self.getnumberofname()[0].click()
        return MemberPage(self.driver)

