class TestJ:
    def setup(self):
        print('only a test')

    def teardown(self):
        print('Done!!!!')

    def test_abc(self):
        a = 1
        assert a == 1
