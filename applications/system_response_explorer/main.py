from basic_systems import amplify, attenuate, shift

if __name__ == "__main__":

    print("1 - Amplify\n2 - Attenuate\n3 - Shift")
    option = input("Choose an option above: ")
    raw_input = input("Enter a number or comma-separated list: ")

    if "," in raw_input:
        x = [float(value.strip()) for value in raw_input.split(",")]
    else:
        x = float(raw_input)

    if option == "1":
        y = amplify(x)
    elif option == "2":
        y = attenuate(x)
    elif option == "3":
        y = shift(x)
    else:
        print("Wrong option choosed! Try again!")

    print(y)
