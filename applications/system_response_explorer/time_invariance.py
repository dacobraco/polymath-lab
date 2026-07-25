from basic_systems import amplify, shift, multiply_by_index
from signal_shifts import delay_one_sample


def is_time_invariant(system, signal):
    system_after_delay = system(delay_one_sample(signal))
    delay_after_system = delay_one_sample(system(signal))

    result = system_after_delay[1:] == delay_after_system[1:]

    print(f"System after delay: {system_after_delay}")
    print(f"Delay after system: {delay_after_system}")
    print(f"{system.__name__.capitalize()} is time invariant: {result}")

    return result


if __name__ == "__main__":
    x = [1, 2, 3, 4]

    is_time_invariant(amplify, x)
    print()
    is_time_invariant(multiply_by_index, x)
    print()
    is_time_invariant(shift, x)