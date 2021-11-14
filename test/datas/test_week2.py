import pytest
import allure
import yaml
from hogwarts.code1.Calculator import Calculator
# cal = Calculator()
# def get_data(keys, level, object):
#     with open('datas/data.yml', encoding='utf-8') as file:
#         file.seek(0)
#         datas = yaml.safe_load(file)
#         data = datas.get(keys)
#         return data.get(level).get(object)

# @allure.title('除法P0级别测试')
# @pytest.mark.div
# @pytest.fixture(params=get_data('div','P0','datas'))
#     #ids=get_data('div','P0','ids')
# def login(request):
#     return request.param
# # @pytest.fixture(params=[[1, 1, 1], [0.1, 0.1, 1], [1, 0.1, 10]])
# # def login(request):
# #     return request.param
# def test_div(login):
#     print(f'{login}')
#     assert cal.div(login[0],login[1]) == login[2]
#
# # def test_div(login):
# #     print(f'{login}')
# #     for i in range(len(login)):
# #         assert cal.div(login[i][0],login[i][1]) == login[i][2]
class TestCal(object):
    @pytest.fixture(scope="class")
    def cal(self):
        return Calculator()
    def get_data(keys, levels, objects):
        with open('data.yml', encoding='utf-8') as file:
            file.seek(0)
            datas = yaml.safe_load(file)
            data = datas.get(keys)
            return data.get(levels).get(objects)
    @allure.title('除法测试')
    @pytest.mark.divfuction
    @pytest.fixture(params=get_data('div', 'P0', 'datas'))
    def getcal(self, request):
        return request.param
    @allure.step('P0')
    def test_div_P0(self, cal, getcal):
        assert cal.div(getcal[0], getcal[1]) == getcal[2]
