import pytest

from multiply import multiply

@pytest.mark.parametrize ("a,b,expected", [
    (1,2,2),
    (8000600,6405006,51243891003600),
    (-1,2,-2),
    (None, None, None),
    (None, 20, 20),
    (30, None, 30),
    (1.4, 1.6, 2.2399999999999998),
    (2 + 4j, 3 +3j, -6 +18j),
])


def test_multiply(a,b,expected):
    assert multiply(a, b) == expected