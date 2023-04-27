import pytest
from challenges.second_challenge_elementary_functions import math


def test_add_function():
    assert math['add']([2, 3, 5, 7, 9]) == 26
    assert math['add']([20, -4, 7, 6, 2]) == 31
    assert math['add']([1]) == 1
    assert math['add']([]) == 0

    with pytest.raises(TypeError):
        math['add'](12)

    with pytest.raises(ValueError):
        math['add']([1, 2, 3, '4'])


def test_sub_function():
    assert math['sub']([8, 2, 1, 3, 5]) == -3
    assert math['sub']([20, -4, 7, 6, 2]) == 9
    assert math['sub']([1]) == 1
    assert math['sub']([]) == 0

    with pytest.raises(TypeError):
        math['sub'](12)

    with pytest.raises(ValueError):
        math['sub']([1, 2, 3, '4'])


def test_div_function():
    assert math['div'](9, 3) == 3
    assert math['div'](22, 2) == 11
    assert math['div'](0, 12) == 0

    with pytest.raises(ZeroDivisionError):
        assert math['div'](3, 0)

    with pytest.raises(TypeError):
        math['div'](12, '4')


def test_mul_function():
    assert math['mul']([3, 4, 2, 9]) == 216
    assert math['mul']([11, 2, 7, 6]) == 924
    assert math['mul']([1]) == 1
    assert math['mul']([]) == 0

    with pytest.raises(TypeError):
        math['mul'](12)

    with pytest.raises(ValueError):
        math['mul']([1, 2, 3, '4'])
