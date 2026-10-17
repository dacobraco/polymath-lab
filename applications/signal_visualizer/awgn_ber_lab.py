import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

number_of_bits = 100_000
sigma_values = [0.2, 0.3, 0.4, 0.5, 0.6]
ber_values = []
ebn0_db_values = []
theoretical_ber_values = []
rng = np.random.default_rng(42)
QPSK_symbols = []

bits = rng.integers(0, 2, size=(number_of_bits // 2, 2))

for b0, b1 in bits:
    s = ((2*b0 - 1) + 1j * (2*b1 - 1)) / np.sqrt(2)
    QPSK_symbols.append(s)

QPSK_symbols = np.array(QPSK_symbols)

for sigma in sigma_values:
    noise_I = rng.normal(0, sigma, size=len(QPSK_symbols))
    noise_Q = rng.normal(0, sigma, size=len(QPSK_symbols))
    noise = noise_I + 1j * noise_Q
    received_symbols = QPSK_symbols + noise
    I_bits = np.where(received_symbols.real > 0, 1, 0)
    Q_bits = np.where(received_symbols.imag > 0, 1, 0)
    received = np.column_stack((I_bits, Q_bits))
    error_count = np.sum(bits != received)
    BER = error_count / bits.size
    ber_values.append(BER)
    ebn0_linear = 1 / (4 * sigma**2)
    ebn0_db = 10 * np.log10(ebn0_linear)
    ebn0_db_values.append(ebn0_db)
    theoretical_ber = 0.5 * erfc(np.sqrt(ebn0_linear))
    theoretical_ber_values.append(theoretical_ber)
    print("Sigma:", sigma, "\tBER:", BER, "\tEb/N0:", ebn0_db)

ebn0_db = 0
ebn0_linear = 10 ** (ebn0_db / 10)

theoretical_ber = 0.5 * erfc(np.sqrt(ebn0_linear))
print("Theoretical BER:", theoretical_ber)

plt.figure()
plt.semilogy(sigma_values, ber_values, marker="o")
plt.xlabel("Sigma")
plt.ylabel("BER")
plt.grid(True, which="both")

plt.figure()
plt.semilogy(ebn0_db_values, ber_values, marker="o", label="Simulation")
plt.semilogy(ebn0_db_values, theoretical_ber_values, marker="o", label="Theoretical")
plt.xlabel("Eb/N0 [dB]")
plt.ylabel("BER")
plt.title("QPSK BER over AWGN Channel")
plt.grid(True, which="both")
plt.legend()
plt.show()
