from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker
import time
from selenium.common.exceptions import NoSuchElementException

from hogwarts.appium.contactpage import ContactPage

"""
前提条件：

1、提前注册企业微信管理员帐号
2、手机端安装企业微信
3、企业微信 app 处于登录状态
通讯录添加成员用例步骤
"""


class TestContact:
    def setup_class(self):
        # pip install Faker
        self.fake = Faker("zh_CN")
        # 初始化操作：打开应用
        desire_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            # 重要的：通过命令获取package/activity :
            # adb logcat ActivityManager:I | grep "cmp"
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            # 跳过设备初始化 ,跳过settings.apk的安装与设置
            "skipDeviceInitialization": True,
            # 跳过uiautomato2 服务安装
            "skipServerInstallation": True,
            # 在运行测试之前，不停止 app ，或者说不重新启动app，
            # 之前在哪个页面上，就在那个页面上继续执行
            # "dontStopAppOnReset": True,
            # 防止 清缓存数据
            "noReset": "True",
            # 等待页面处于idle状态 ，默认10s
            "settings[waitForIdleTimeout]": 0
        }
        # 客户端与服务端建立连接的关键语句
        # 启动app
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        # 隐式等待，每一次查找元素的时候，动态的查找
        self.driver.implicitly_wait(8)

    def back(self, num=3):
        for i in range(num):
            self.driver.back()

    def teardown(self):
        self.back()

    def teardown_class(self):
        # 关闭应用
        self.driver.quit()

    def test_delmember(self):
        list = []
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/j3d").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='搜索']").send_keys('acc')
        # if self.driver.find_element(MobileBy.XPATH,"//*[@text='查看更多联系人']"):
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='查看更多联系人']").click()
        #获取一共有多少个名字
        list = self.driver.find_elements(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/bgo']")
        numberofnames = len(list)
        self.driver.find_elements(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/bgo']")[-1].click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/j2z").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
        time.sleep(10)
        #获取删除后有多少个名字
        list2 = self.driver.find_elements(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/bgo']")
        delmember_result = len(list2)
        #检查删除后有多少个名字
        assert (numberofnames -1) == delmember_result
