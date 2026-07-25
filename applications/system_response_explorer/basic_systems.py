def amplify(x):
    if isinstance(x, list):
        return [2 * value for value in x]
    return 2 * x

def attenuate(x):
    if isinstance(x, list):
        return [0.5 * value for value in x]
    return 0.5 * x

def shift(x):
    if isinstance(x, list):
        return [value + 3 for value in x]
    return x + 3