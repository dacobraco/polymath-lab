import numpy as np

fs = 100.0
rng = np.random.default_rng(42)

t = np.arange(0, 3, 1 / fs)
noise_mask = t < 1
active_mask = t >= 1

s = np.zeros_like(t)
s[active_mask] = np.sin(2 * np.pi * 5 * t[active_mask])

def run_case(label, active_sigma):
    v = rng.normal(0, 0.2, len(t))
    v[active_mask] = rng.normal(0, active_sigma, np.sum(active_mask))

    x = s + v

    estimated_noise_power = np.mean(x[noise_mask] ** 2)
    active_total_power = np.mean(x[active_mask] ** 2)
    estimated_signal_power = active_total_power - estimated_noise_power

    if estimated_signal_power > 0:
        estimated_snr = estimated_signal_power / estimated_noise_power
        estimated_snr_db = 10 * np.log10(estimated_snr)
    else:
        estimated_snr = np.nan
        estimated_snr_db = np.nan

    true_signal_power = np.mean(s[active_mask] ** 2)
    true_noise_power = np.mean(v[active_mask] ** 2)
    true_snr = true_signal_power / true_noise_power
    true_snr_db = 10 * np.log10(true_snr)

    error_db = estimated_snr_db - true_snr_db

    print(label)
    print(f"Estimated noise power: {estimated_noise_power}")
    print(f"Estimated signal power: {estimated_signal_power}")
    print(f"Estimated SNR: {estimated_snr_db} dB")
    print(f"True noise power: {true_noise_power}")
    print(f"True signal power: {true_signal_power}")
    print(f"True SNR: {true_snr_db} dB")
    print(f"Estimation error: {error_db} dB")
    print()

run_case("STATIONARY NOISE", 0.2)
run_case("CHANGING NOISE", 0.5)
