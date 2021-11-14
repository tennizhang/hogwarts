import logging

import pytest
from hogwarts.code1.Calculator import Calculator
import yaml

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
            return data.get(levels).get(objects

    @pytest.mark.run(2)
    @pytest.fixture(params=get_data('add', 'P0', 'datas'))
    def getcal(self, request):
        return request.param

    def test_add_P0(self, cal, getcal):
        assert cal.add(getcal[0], getcal[1]) == getcal[2]

    @pytest.mark.run(0)
    @pytest.fixture(params=get_data('add', 'P1_1', 'datas'))
    def getcal(self, request):
        return request.param

    def test_add_P1_1(self, cal, getcal):
        assert cal.add(getcal[0], getcal[1]) == getcal[2]

    @pytest.mark.run(1)
    @pytest.fixture(params=get_data('add', 'P1_2', 'datas'))
    def getcal(self, request):
        return request.param

    def test_add_P1_2(self, cal, getcal):
        assert cal.add(getcal[0], getcal[1]) == getcal[2]

    @pytest.mark.run(4)
    @pytest.fixture(params=get_data('add', 'P2', 'datas'))
    def getcal(self, request):
        return request.param

    def test_add_P2(self, cal, getcal):
        assert cal.add(getcal[0], getcal[1]) == getcal[2]

    @pytest.mark.run(3)
    @pytest.fixture(params=get_data('div', 'P0', 'datas'))
    def getcal(self, request):
        return request.param

    def test_div_P0(self, cal, getcal):
        assert cal.div(getcal[0], getcal[1]) == getcal[2]
