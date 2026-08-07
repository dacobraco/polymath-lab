import numpy as np
from convolution import manual_convolution

def test_manual_known_example():
    x = [2, -1, 3]
    h = [1, 2, -1]
    expected = [2, 3, -1, 7, -3]
    result = manual_convolution(x, h)
    assert np.allclose(result, expected)

def test_convolution_is_commutative():
    x = [2, -1, 3]
    h = [1, 2, -1]
    result1 = manual_convolution(x, h)
    result2 = manual_convolution(h, x)
    assert np.allclose(result1, result2)

def test_output_length():
    x = [2, -1, 3]
    h = [1, 2, -1]
    y = manual_convolution(x, h)
    assert len(y) == len(x) + len(h) - 1
