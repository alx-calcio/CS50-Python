import pytest

"""
from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
    try:
        assert square(-1) == 1
    except AssertionError:
        print("-1 squared was not 1")


if __name__ == "__main__":
    main()
"""

from calculator import square


def test_zero():
    assert square(0) == 0


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_str():
    with pytest.raises(
        TypeError
    ):  # on s'attend à ce que ça fasse ça et on marque une erreur sinon
        square("cat")
