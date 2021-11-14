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

    def test_div_P0(self, cal, getcal, cal_log):
        assert cal.div(getcal[0], getcal[1]) == getcal[2]

    # 配置log文件名称
    def pytest_configure(config):
        time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # time_now = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        config.option.log_file = os.path.join(config.rootdir, 'logs', f'{time_now}.log')