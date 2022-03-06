import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestBaidu:
    def setup(self):
        url = 'https://www.baidu.com/'
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        time.sleep(3)

    def test_search(self):
        self.driver.find_element(By.ID,"kw").send_keys('felicity')
        time.sleep(3)
        self.driver.find_element(By.ID, "su").click()
