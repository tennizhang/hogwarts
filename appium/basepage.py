from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from faker import Faker
import logging
from appium.webdriver.common.mobileby import MobileBy




class BasePage:
        def __init__(self, driver:WebDriver=None):
                self.driver = driver

        def start_app(self):
                if self.driver == None:
                        logging.info(f'driver is {self.driver}')
                        self._base_url = None
                        self.fake = Faker("zh_CN")
                        self.capability = {}
                        self.capability['platformName'] = 'Android'
                        self.capability['deviceName'] = 'emulator-5554'
                        self.capability['autoGrantPermissions'] = True
                        self.capability['appPackage'] = 'com.tencent.wework'
                        self.capability['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
                        self.capability['noReset'] = True
                        self.capability['skipServerInstallation'] = True
                        self.capability['unicodeKeyBoard'] = True
                        self.capability['resetKeyBoard'] = True
                        self.capability['skipDeviceInitialization'] = True
                        self.capability['dontStopAppOnReset'] = True
                        self.capability['settings[waitForIdleTimeout]'] = 0

                        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.capability)
                else:
                        self.driver.launch_app()
                self.driver.implicitly_wait(10)
                self.size = self.driver.get_window_size()

                return self

        def goto_main(self):
                from hogwarts.appium.mainpage import MainPage
                return MainPage(self.driver)

        def xpath(self, xpath):
                return self.driver.find_elements(MobileBy.XPATH, xpath)

        def xpathclick(self, xpath):
                self.xpath(xpath).click()

        def sendkey(self, xpath, keys):
                self.xpath(xpath).send_keys(keys)

        def back(self, num=3):
                for i in range(num):
                        self.driver.back()

        def app_back(self):
                self.back()

        def app_stop(self):
                # 关闭应用
                self.driver.quit()



