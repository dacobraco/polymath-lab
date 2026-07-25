from basic_systems import amplify, attenuate, shift
from linearity import is_linear

def test_amplify():
    assert amplify(4) == 8
    assert amplify([1, 2, 3]) == [2, 4, 6]


def test_attenuate():
    assert attenuate(4) == 2
    assert attenuate([1, 2, 3]) == [0.5, 1, 1.5]


def test_shift():
    assert shift(4) == 7
    assert shift([1, 2, 3]) == [4, 5, 6]


def test_linearity():
    assert is_linear(amplify, 2, 4, 3, 2) is True
    assert is_linear(attenuate, 2, 4, 3, 2) is True
    assert is_linear(shift, 2, 4, 3, 2) is False

if __name__ == "__main__":
    test_amplify()
    test_attenuate()
    test_shift()
    test_linearity()

    print("\nAll tests passed!")