
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
number_of_bits = 100_000
p = 0.1

bits = rng.integers(0, 2, number_of_bits)


def hamming_encode(data):
    data_blocks = data.reshape(-1, 4)
    encoded = np.zeros((len(data_blocks), 7), dtype=int)

    encoded[:, [2, 4, 5, 6]] = data_blocks

    encoded[:, 0] = encoded[:, 2] ^ encoded[:, 4] ^ encoded[:, 6]
    encoded[:, 1] = encoded[:, 2] ^ encoded[:, 5] ^ encoded[:, 6]
    encoded[:, 3] = encoded[:, 4] ^ encoded[:, 5] ^ encoded[:, 6]

    return encoded


def hamming_decode(received):
    corrected = received.copy()

    s1 = corrected[:, 0] ^ corrected[:, 2] ^ corrected[:, 4] ^ corrected[:, 6]
    s2 = corrected[:, 1] ^ corrected[:, 2] ^ corrected[:, 5] ^ corrected[:, 6]
    s3 = corrected[:, 3] ^ corrected[:, 4] ^ corrected[:, 5] ^ corrected[:, 6]

    syndromes = s1 + 2*s2 + 4*s3
    error_rows = np.where(syndromes != 0)[0]

    corrected[error_rows, syndromes[error_rows] - 1] ^= 1

    recovered = corrected[:, [2, 4, 5, 6]].reshape(-1)

    return recovered, corrected, syndromes


data = np.array([1, 0, 1, 1])
hamming = hamming_encode(data)[0]

received_hamming = hamming.copy()
received_hamming[5] ^= 1

recovered_data, corrected_hamming, syndrome = hamming_decode(received_hamming.reshape(1, 7))

print("=== HAMMING SINGLE BLOCK TEST ===")
print("Original data:", data)
print("Encoded:", hamming)
print("Received:", received_hamming)
print("Syndrome:", syndrome[0])
print("Corrected:", corrected_hamming[0])
print("Recovered data:", recovered_data)


received_uncoded = bits ^ (rng.random(len(bits)) < p)
ber_uncoded = np.mean(bits != received_uncoded)


encoded_repeat = np.repeat(bits, 3)
error_mask_repeat = rng.random(len(encoded_repeat)) < p
received_repeat = np.bitwise_xor(encoded_repeat, error_mask_repeat)

groups = received_repeat.reshape(-1, 3)
decoded_repeat = (np.sum(groups, axis=1) >= 2).astype(int)

ber_repeat = np.mean(bits != decoded_repeat)


encoded_hamming = hamming_encode(bits)
error_mask_hamming = rng.random(encoded_hamming.shape) < p
received_hamming_blocks = np.bitwise_xor(encoded_hamming, error_mask_hamming)

decoded_hamming, corrected_blocks, syndromes = hamming_decode(received_hamming_blocks)

ber_hamming = np.mean(bits != decoded_hamming)


print("\n=== BER COMPARISON ===")
print("Uncoded BER:", ber_uncoded)
print("Repetition BER:", ber_repeat)
print("Hamming BER:", ber_hamming)

print("\n=== CODE RATES ===")
print("Uncoded:", 1.0)
print("Repetition (3,1):", 1/3)
print("Hamming (7,4):", 4/7)

print("\n=== TRANSMITTED BITS ===")
print("Uncoded:", len(bits))
print("Repetition:", len(encoded_repeat))
print("Hamming:", encoded_hamming.size)

print("\n=== HAMMING DIAGNOSTICS ===")
print("Hamming blocks:", encoded_hamming.shape)
print("Nonzero syndromes:", np.count_nonzero(syndromes))
print("Remaining bit errors:", np.count_nonzero(bits != decoded_hamming))


labels = ["Uncoded", "Repetition (3,1)", "Hamming (7,4)"]
ber_values = [ber_uncoded, ber_repeat, ber_hamming]

plt.figure(figsize=(9, 5))
bars = plt.bar(labels, np.array(ber_values) * 100)

plt.ylabel("Bit Error Rate (%)")
plt.title("Channel Coding Comparison - BSC, p = 0.1")
plt.grid(axis="y", alpha=0.3)

for bar, value in zip(bars, ber_values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f"{value*100:.2f}%", ha="center")

plt.tight_layout()
plt.show()
