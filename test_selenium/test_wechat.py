import pytest
import time
import yaml
from selenium import webdriver

from hogwarts.test_selenium.MainPage import MainPage


class TestWechat():

    def test_wechat(self):
        name, num, phonenum = 'adey', '1234', '11001624711'
        result = MainPage().goto_add_member().add_menmber(name, num, phonenum)