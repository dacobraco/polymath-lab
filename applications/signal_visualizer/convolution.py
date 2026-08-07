import numpy as np
import matplotlib.pyplot as plt

def manual_convolution(x, h):
    y = np.zeros(len(x) + len(h) - 1)
    for i in range(len(x)):
        for j in range(len(h)):
            y[i + j] += x[i] * h[j]
    return y


def parse_sequence(raw_input):
    numbers = list(map(float, raw_input.split(',')))
    return numbers

if __name__ == "__main__":
    x = parse_sequence(input("Enter x[n] as comma-separated values:"))
    h = parse_sequence(input("Enter h[n] as comma-separated values:"))

    y = manual_convolution(x, h)
    y1 = manual_convolution(h, x)
    numpy_result = np.convolve(x, h)

    print("Manual convolution:", y)
    print("NumPy convolution:", numpy_result)
    print("Matching:", np.allclose(y, numpy_result))
    print("Convolution is commutative:", np.allclose(y, y1))

    fig1, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 7))
    axes[0].stem(range(len(x)), x)
    axes[1].stem(range(len(h)), h)
    axes[2].stem(range(len(y)), y)
    axes[0].set_ylabel("Amplitude")
    axes[1].set_ylabel("Amplitude")
    axes[2].set_ylabel("Amplitude")
    axes[0].set_title("Input x[n]")
    axes[1].set_title("Impulse response h[n]")
    axes[2].set_title("Output y[n]")
    axes[2].set_xlabel("n")

    for ax in axes:
        ax.grid(True)

    contributions = np.zeros((len(x), len(y)))

    for i in range(len(x)):
        for j in range(len(h)):
            contributions[i, i + j] = x[i] * h[j]


    contribution_sum = np.sum(contributions, axis=0)
    print("Contribution sum:", contribution_sum)
    print("Matching:", np.allclose(contribution_sum, y))
    print(contributions)

    fig2, axes2 = plt.subplots(len(x) + 1, 1, sharex=True, figsize=(8, 10))
    for ax2 in range(len(x)):
        axes2[ax2].stem(range(len(y)), contributions[ax2])
        axes2[ax2].set_title(f"Contribution from x[{ax2}]")

    axes2[-1].stem(range(len(y)), contribution_sum)
    axes2[-1].set_title("Sum of contributions = y[n]")
    axes2[-1].set_xlabel("n")

    for ax2 in range(len(axes2)):
        axes2[ax2].grid(True)
        axes2[ax2].set_ylabel("Amplitude")

    fig1.tight_layout()
    fig2.tight_layout()
    plt.show()
