def delay_one_sample(signal):
    delayed_signal = [0] + signal[:-1]
    return delayed_signal


def advance_one_sample(signal):
    advanced_signal = signal[1:] + [0]
    return advanced_signal


if __name__ == "__main__":
    x = [1, 2, 3, 4]

    print(f"Input: {x}")
    print(f"Delayed: {delay_one_sample(x)}")
    print(f"Advanced: {advance_one_sample(x)}")