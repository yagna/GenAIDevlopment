from math_learning.my_math import add


def test_add():
    assert add(6,9) == 15

def test_add_wrong():
    assert add(4,6) == 11
    