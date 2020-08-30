import pytest

from add import add

@pytest.mark.parametrize("a,b, expected", [
    (1,2,3),
    (8000600,6405006,14405606),
    (-1,2,1),
    (None, None, None),
    (None, 20, 20),
    (30, None, 30),
    (1.4, 1.6, 3.0),
    (2 + 4j, 3 +3j, 5 +7j),
    (3 ** 100, 55 ** 55, 524744532468751923546122657597368049278513737089550649578056654999644138812068513480801472756376)
])

def test_add(a,b,expected):
    assert add(a, b) == expected

def test_add_characters():
    return_value = add(1, 2)
    print(type(return_value))
    assert return_value == 3

def test_add_float():
    return_value = add(1.5, 2)
    print(type(return_value))
    assert return_value == 3.5

def test_add_negative():
    return_value = add(-1, 2)
    print(type(return_value))
    assert return_value == 1

def test_add_null():
    return_value = add(None, None)
    print(type(return_value))
    assert return_value == None

def test_add_space():
    return_value = add("","" )
    print(type(return_value))
    assert return_value == ""

