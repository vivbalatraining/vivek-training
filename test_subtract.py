import pytest

from subtract import subtract

def test_subtract_elementary():
    assert subtract(2, 1) == 1

def test_subtract_high_school():
    assert subtract(8000600, 6405006) == 1595594

def test_subtract_characters():
    return_value = subtract("2", "1")
    print(type(return_value))
    assert return_value == 3

def test_subtract_float():
    return_value = subtract(1.5, 2)
    print(type(return_value))
    assert return_value == 3.5

def test_subtract_negative():
    return_value = subtract(-1, 2)
    print(type(return_value))
    assert return_value == -3

def test_subtract_null():
    return_value = subtract(null, null)
    print(type(return_value))
    assert return_value == null

def test_subtract_space():
    return_value = subtract("","" )
    print(type(return_value))
    assert return_value == ""
