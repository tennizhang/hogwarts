import time

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
        list = self.driver.find_elements(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bgo']")
        return list

    def numberofnames(self):
        numberofnames = len(self.getnumberofname())
        return numberofnames

    def searchmember(self, membername):
        from hogwarts.appium.memberpage import MemberPage
        #点击搜索按钮
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/j3d").click()
        #搜索用户
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(membername)
        self.getnumberofname()[0].click()
        return MemberPage()

