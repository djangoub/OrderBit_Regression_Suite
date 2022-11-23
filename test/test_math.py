import pytest


def add_numbers(a, b):
    return a + b


@pytest.mark.math
def test_add_small_numbers():
    assert add_numbers(1, 2) == 3, "Add numbers should be 3"


@pytest.mark.math
def test_add_large_numbers():
    assert add_numbers(400, 300) == 700, "Add numbers should be 700"
