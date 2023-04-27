import pytest
from challenges.second_challenge_elementary_functions import math


def test_add_function():
    add = math['add']

    assert add([2, 3, 5, 7, 9]) == 26
    assert add([20, -4, 7, 6, 2]) == 31
    assert add([1]) == 1
    assert add([]) == 0

    with pytest.raises(TypeError):
        add(12)

    with pytest.raises(ValueError):
        add([1, 2, 3, '4'])


def test_sub_function():
    sub = math['sub']

    assert sub([8, 2, 1, 3, 5]) == -3
    assert sub([20, -4, 7, 6, 2]) == 9
    assert sub([1]) == 1
    assert sub([]) == 0

    with pytest.raises(TypeError):
        sub(12)

    with pytest.raises(ValueError):
        sub([1, 2, 3, '4'])


def test_div_function():
    div = math['div']

    assert div(9, 3) == 3
    assert div(22, 2) == 11
    assert div(0, 12) == 0

    with pytest.raises(ZeroDivisionError):
        assert div(3, 0)

    with pytest.raises(TypeError):
        div(12, '4')


def test_mul_function():
    mul = math['mul']

    assert mul([3, 4, 2, 9]) == 216
    assert mul([11, 2, 7, 6]) == 924
    assert mul([1]) == 1
    assert mul([]) == 0

    with pytest.raises(TypeError):
        mul(12)

    with pytest.raises(ValueError):
        mul([1, 2, 3, '4'])
