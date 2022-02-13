import yaml
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class BasePage:
    _base_url = None
    def __init__(self, basedriver=None):
        if basedriver:
            self.driver = basedriver
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        if self._base_url != None:
            self.driver.get(self._base_url)
            # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
            cookie = yaml.safe_load(open("cookie.yaml"))
            # 3. 植入cookie
            for c in cookie:
                self.driver.add_cookie(c)
            time.sleep(3)
            # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
            self.driver.get(self._base_url)
        else:
            # 如果url 为空，那么抛出异常
            pass

    def find(self, by, locaotr=None):
        """
        点击操作， 需要兼容两种情况
        :return:
        """
        # 如果传入一个参数，证明是元祖
        if locaotr == None:
            # xxx((1, 2)) -> xxx(*(1,2))->xxx(1,2)
            # 如果传入元祖，则做解包操作
            res = self.driver.find_element(*by)
        # 如果传入两个参数，证明是分开传递的
        else:
            res = self.driver.find_element(by, locaotr)
        print(f"找到的元素为{res}")
        return res

    def finds(self):
        pass





