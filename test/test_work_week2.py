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
        assert cal.add(getcal_P0[0], getcal_P0[1]) == getcal_P0[2]

    @pytest.mark.run(0)
    def test_add_P1_1(self, cal, getcal_P1_1):
        with pytest.raises(eval(getcal_P1_1[2])) as e:
            result = cal.div(getcal_P1_1[0], getcal_P1_1[1])
        # 期望的异常与实际异常比对
        assert getcal_P1_1[2] == e.typename
        # assert cal.add(getcal_P1_1[0], getcal_P1_1[1]) == getcal_P1_1[2]

    @pytest.mark.run(1)
    def test_add_P1_2(self, cal, getcal_P1_2):
        assert cal.add(getcal_P1_2[0], getcal_P1_2[1]) == getcal_P1_2[2]

    @pytest.mark.run(4)
    def test_add_P2(self, cal, getcal_P2):
        assert cal.add(getcal_P2[0], getcal_P2[1]) == getcal_P2[2]

    @pytest.mark.run(3)
    def test_div_P0(self, cal, getcal_DIV):
        assert cal.div(getcal_DIV[0], getcal_DIV[1]) == getcal_DIV[2]
