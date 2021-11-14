import logging

import pytest
from hogwarts.code1.Calculator import Calculator
import yaml
import datetime

class TestCal():
    @pytest.fixture(scope="class", autouse=True)
    def cal(self):
        yield Calculator()
        print('测试结束')

    @pytest.fixture(autouse=True)
    def cal_start(self):
        print('开始计算')
        yield print('结束计算')

    def get_data(keys, levels, objects):
        with open('./datas/data.yml', encoding='utf-8') as file:
            file.seek(0)
            datas = yaml.safe_load(file)
            data = datas.get(keys)
            return data.get(levels).get(objects)

    @pytest.fixture(params=get_data('div', 'P0', 'datas'))
    def getcal(self, request):
        return request.param


    def test_div_P0(self, cal, getcal):
        assert cal.div(getcal[0], getcal[1]) == getcal[2]
        # logging.info('数据'{getcal[0], getcal[1]},'结果'getcal[2])

