import pytest
from hogwarts.code1.Calculator import Calculator
import yaml


path= 'datas/data.yml'
cal = Calculator()
def get_data(keys,level,object):
    with open(path, encoding='utf-8') as file:
        file.seek(0)
        datas = yaml.safe_load(file)
        add_datas = datas.get(keys)
        return (add_datas.get(level).get(object),add_datas.get(level).get(object))
        print(datas)

class TestCalculator:
    @pytest.mark.P0
    @pytest.mark.parametrize('a, b, result', get_data('add','P0','datas')[0], ids=get_data('add','P0','ids')[1])
    def test_p1(self, a, b, result):
        assert cal.add(a, b) == result
    @pytest.mark.P1
    @pytest.mark.parametrize('a, b, result', get_data('add','P1_2','datas')[0], ids=get_data('add','P1_2','ids')[1])
    def test_p12(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.cal.div(a,b)
        assert expect == e.typename
#     def setup(self):
#         print('开始计算')
#     def teardown(self):
#         print('结束计算')
#     def teardown_class(self):
#         print('结束运算')
#     @pytest.mark.parametrize('a,b,result',[(1,1,2),(-0.01,0.02,0.01),(10,0.02,10.02)])

#     # def test_add001(self):
#     #     c = cal.add(1, 1)
#     #     assert c==2
#     #
#     # def test_add_002(self):
#     #     c = cal.add(-0.01, 0.02)
#     #     assert c==0.01
#     #
#     #
#     # def test_add_003(self):
#     #     c = cal.add(10, 0.02)
#     #     assert c==10.02

