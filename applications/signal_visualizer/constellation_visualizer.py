import numpy as np
import matplotlib.pyplot as plt

sigma = 0.8
rng = np.random.default_rng(42)
bits = rng.integers(0, 2, 1000)
bit_blocks = bits.reshape(-1, 2)

a = bit_blocks[:, 0]
I = 2*a - 1
b = bit_blocks[:, 1]
Q = 2*b - 1

noise_i = rng.normal(0, sigma, len(I))
noise_q = rng.normal(0, sigma, len(Q))

I_rx = I + noise_i
Q_rx = Q + noise_q

decoded_I = np.where(I_rx > 0, 1, 0)
decoded_Q = np.where(Q_rx > 0, 1, 0)

print("I decoded 100% successfully:", np.all(a == decoded_I))
print("Q decoded 100% successfully:", np.all(b == decoded_Q))

wrong_bits_count = np.sum(a != decoded_I) + np.sum(b != decoded_Q)
wrong_symbols_count = np.sum(np.logical_or(a != decoded_I, b != decoded_Q))

ber = wrong_bits_count / len(bits)
ser = wrong_symbols_count / len(bit_blocks)

print("BER:", ber*100, "%")
print("SER:", ser*100, "%")

plt.scatter(I_rx, Q_rx, alpha=0.5)
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True)

#################

sigma_qam = 0.8
new_bits = rng.integers(0, 2, 1000)
new_blocks = new_bits.reshape(-1, 4)
levels = np.array([-3, -1, 3, 1])
choices = np.array([-3, -1, 1, 3])
A = new_blocks[:, :2]
B = new_blocks[:, 2:4]
I_index = 2*A[:, 0] + A[:, 1]
Q_index = 2*B[:, 0] + B[:, 1]
new_I = levels[I_index]
new_Q = levels[Q_index]

I_qam_rx = rng.normal(0, sigma_qam, len(new_I)) + new_I
Q_qam_rx = rng.normal(0, sigma_qam, len(new_Q)) + new_Q

conditions_I = [
    I_qam_rx < -2,
    (I_qam_rx >= -2) & (I_qam_rx < 0),
    (I_qam_rx >= 0) & (I_qam_rx < 2),
    I_qam_rx >= 2
]

conditions_Q = [
    Q_qam_rx < -2,
    (Q_qam_rx >= -2) & (Q_qam_rx < 0),
    (Q_qam_rx >= 0) & (Q_qam_rx < 2),
    Q_qam_rx >= 2
]

I_qam_decoded = np.select(conditions_I, choices)
Q_qam_decoded = np.select(conditions_Q, choices)

print("I errors:", np.count_nonzero(new_I != I_qam_decoded))
print("Q errors:", np.count_nonzero(new_Q != Q_qam_decoded))

sigma = 0.8

qpsk_rx = np.column_stack((I, Q)) + rng.normal(0, sigma, (len(I), 2))
qam_rx = np.column_stack((new_I, new_Q)) / np.sqrt(5) + rng.normal(0, sigma, (len(new_I), 2))

qam_decoded = np.array([-3, -1, 1, 3])[np.digitize(qam_rx * np.sqrt(5), [-2, 0, 2])]
qam_bits = np.column_stack((qam_decoded[:, 0] > 0, np.abs(qam_decoded[:, 0]) == 1, qam_decoded[:, 1] > 0, np.abs(qam_decoded[:, 1]) == 1))

print(f"QPSK BER: {100 * np.mean((qpsk_rx > 0) != bit_blocks):.2f}%")
print(f"16-QAM BER: {100 * np.mean(qam_bits != new_blocks):.2f}%")

plt.figure()
plt.scatter(qam_rx[:, 0], qam_rx[:, 1])
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True)
plt.show()