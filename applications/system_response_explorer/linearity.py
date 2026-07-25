from basic_systems import amplify, attenuate, shift


def is_linear(system, x1, x2, a, b):
    left = system(a * x1 + b * x2)
    right = a * system(x1) + b * system(x2)

    result = left == right

    print(f"{system.__name__.capitalize()} is linear: {result}")
    return result

if __name__ == "__main__":
    option = input(
        "1. Amplify\n"
        "2. Attenuate\n"
        "3. Shift\n\n"
        "Choose your option (1, 2 or 3): "
    )

    if option == "1":
        system = amplify
    elif option == "2":
        system = attenuate
    elif option == "3":
        system = shift
    else:
        system = None
        print("Invalid option.")

    if system is not None:
        x1, x2 = map(int, input("Enter x1 and x2: ").split())
        a, b = map(int, input("Enter coefficients a and b: ").split())

        is_linear(system, x1, x2, a, b)