import pytest
from random import randint


class TestLogin:

    def test_login1(self):
        print("这是测试1")
        assert 1

    @pytest.mark.run(order=1)
    def test_login2(self):
        num = randint(1, 5)
        if num == 1:
            assert 1
        else:
            assert 0
