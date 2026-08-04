from basic_systems import amplify, attenuate, shift, multiply_by_index, add_previous_sample
from linearity import is_linear
from signal_shifts import delay_one_sample, advance_one_sample
from time_invariance import is_time_invariant

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


def test_signal_shifts():
    x = [1, 2, 3, 4]
    assert delay_one_sample(x) == [0, 1, 2, 3]
    assert advance_one_sample(x) == [2, 3, 4, 0]


def test_time_invariance():
    x = [1, 2, 3, 4]
    assert is_time_invariant(amplify, x) is True
    assert is_time_invariant(attenuate, x) is True
    assert is_time_invariant(shift, x) is True
    assert is_time_invariant(multiply_by_index, x) is False


def test_add_previous_sample():
    x = [1, 2, 3, 4]
    assert add_previous_sample(x) == [1, 3, 5, 7]
    assert add_previous_sample([]) == []

if __name__ == "__main__":
    test_amplify()
    test_attenuate()
    test_shift()
    test_linearity()
    test_signal_shifts()
    test_time_invariance()
    test_add_previous_sample()

    print("\nAll tests passed!")