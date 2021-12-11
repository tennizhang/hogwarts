from hogwarts.appium.basepage import BasePage
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hogwarts.appium.contactpage import ContactPage
from hogwarts.appium.workstudiopage import WorkStudioPage

class MainPage(BasePage):
    def getintocontactpage(self):
        self.xpathclick("//*[@text='通讯录']")
        return ContactPage()

    def gotoWSpage(self):
        self.xpathclick("//*[@text='工作台']")
        return WorkStudioPage()