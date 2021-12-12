import logging

from hogwarts.appium.basepage import BasePage
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hogwarts.appium.contactpage import ContactPage
from hogwarts.appium.workstudiopage import WorkStudioPage

class MainPage(BasePage):
    def getintocontactpage(self):
        self.xpathclick("//*[@text='通讯录']")
        logging.info(f'点击通讯录')
        return ContactPage(self.driver)

    def gotoWSpage(self):
        self.xpathclick("//*[@text='工作台']")
        logging.info(f'点击工作台')
        return WorkStudioPage(self.driver)