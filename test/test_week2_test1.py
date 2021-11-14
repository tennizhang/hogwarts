import pytest
from hogwarts.code1.Calculator import Calculator
import yaml
import datetime

class TestCal():
    @pytest.fixture(scope='class',autouse=True)
    def cal(self):
        return Calculator()

    @pytest.fixture(autouse=True)
    def cal_start(self):
        print('开始计算')

    @pytest.fixture(autouse=True)
    def cal_stop(self):
        yield print('结束计算')

    @pytest.fixture(scope='class',autouse=True)
    def cal_end(self):
        yield print('测试结束')

    @pytest.fixture()
    def cal_log(self):
        with open(f'./logs/{datetime.datetime.now}.log','w+') as file:
            file.write()

    def get_data(keys, levels, objects):
        with open('./datas/data.yml', encoding='utf-8') as file:
            file.seek(0)
            datas = yaml.safe_load(file)
            data = datas.get(keys)
            return data.get(levels).get(objects)

    @pytest.fixture(params=get_data('div', 'P0', 'datas'))
    def getcal(self, request):
        return request.param

    def test_div_P0(self, cal, getcal, cal_log):
        assert cal.div(getcal[0], getcal[1]) == getcal[2]