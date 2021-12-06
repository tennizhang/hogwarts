from selenium.common.exceptions import NoSuchElementException
from hogwarts.appium.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy

class WorkStudioPage(BasePage):
    def findcheckinfunction(self, text, num=5):
        for i in range(num):
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                return ele
            except:
                # 滑动操作
                # 获取屏幕的尺寸 'width', 'height'
                # 屏幕宽
                width = self.size.get("width")
                # 屏幕高
                height = self.size.get("height")
                # 起点x
                start_x = width / 2
                # 起点y  屏幕的y*0.8
                start_y = height * 0.8
                # 终点x
                end_x = start_x
                # 终点y
                end_y = height * 0.2
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num - 1:
                raise NoSuchElementException(f"找了{num}次，未找到")

    def checkinoutside(self, text):
        self.findcheckinfunction(text).click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()

    def checkinoutsidesucc(self):
        checkinout_result = self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
        return checkinout_result











