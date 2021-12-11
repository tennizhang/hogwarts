from appium import webdriver
from faker import Faker

from appium.webdriver.common.mobileby import MobileBy

class BasePage:
        def start_app(self, basedriver=None):
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
                if basedriver:
                        self.driver = basedriver
                else:
                        # if self._base_url != None:
                        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.capability)
                        # else:
                        #         raise Exception
                self.driver.implicitly_wait(10)
                self.size = self.driver.get_window_size()

        def xpath(self, xpath):
                self.driver.find_elements(MobileBy.XPATH, xpath)

        def xpathclick(self, xpath):
                self.driver.find_elements(MobileBy.XPATH, xpath).click()

        def sendkey(self, xpath, keys):
                self.driver.find_elements(MobileBy.XPATH, xpath).send_keys(keys)

        def back(self, num=3):
                for i in range(num):
                        self.driver.back()

        def app_back(self):
                self.back()

        def app_stop(self):
                # 关闭应用
                self.driver.quit()



