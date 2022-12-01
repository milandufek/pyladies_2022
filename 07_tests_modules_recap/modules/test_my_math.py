from my_math import sum, multiply, milans_theorem


def test_sum_ok():
    assert sum(1, 2) == 3


def test_sum_not_ok():
    a = 10
    b = 15
    result = sum(a, b)
    assert result != 90


def test_multilication():
    assert multiply(5, 5) == 25
    assert multiply(4, 1) == 4
    assert multiply(-2, 8) == -16
    assert multiply(-20, -2) == 40


def test_milans_theorem():
    assert milans_theorem(1, 2, 3) == 4
