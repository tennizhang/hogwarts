import pytest
from hogwarts.code1.Calculator import Calculator

class TestCal():
    @pytest.fixture(scope="class", autouse=True)
    def cal(self):
        yield Calculator()
        print('测试结束')

    @pytest.fixture(autouse=True)
    def cal_start(self):
        print('开始计算')
        yield print('结束计算')

    @pytest.mark.run(2)
    def test_add_P0(self, cal, getcal_P0):
        assert cal.add(getcal[0], getcal[1]) == getcal[2]

    @pytest.mark.run(0)
    def test_add_P1_1(self, cal, getcal_P1_1):
        assert cal.add(getcal[0], getcal[1]) == getcal[2]

    @pytest.mark.run(1)
    def test_add_P1_2(self, cal, getcal_P1_2):
        assert cal.add(getcal[0], getcal[1]) == getcal[2]

    @pytest.mark.run(4)
    def test_add_P2(self, cal, getcal_P2):
        assert cal.add(getcal[0], getcal[1]) == getcal[2]

    @pytest.mark.run(3)
    def test_div_P0(self, cal, getcal_DIV):
        assert cal.div(getcal[0], getcal[1]) == getcal[2]
