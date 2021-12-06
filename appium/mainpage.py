from hogwarts.appium.basepage import BasePage
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hogwarts.appium.contactpage import ContactPage
from hogwarts.appium.workstudiopage import WorkStudioPage

class MainPage(BasePage):
    # _base_url = f"'http://localhost:4723/wd/hub', {BasePage().capability}"
    def getintocontactpage(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactPage()

    def gotoWSpage(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()

        return WorkStudioPage()