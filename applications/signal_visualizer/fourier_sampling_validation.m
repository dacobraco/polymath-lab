clear;
clc;
close all;

signal_frequency = 3;
sample_rate = 12;
reference_rate = 2000;
duration = 1;
phase = 0;

sample_interval = 1 / sample_rate;

reference_time = 0:(1 / reference_rate):(duration - 1 / reference_rate);
sample_time = 0:sample_interval:(duration - sample_interval);

reference_signal = sin(2 * pi * signal_frequency * reference_time + phase);
sampled_signal = sin(2 * pi * signal_frequency * sample_time + phase);

zoh_signal = interp1(sample_time, sampled_signal, reference_time, "previous", "extrap");
linear_signal = interp1(sample_time, sampled_signal, reference_time, "linear", "extrap");

zoh_signal(reference_time > sample_time(end)) = sampled_signal(end);
linear_signal(reference_time > sample_time(end)) = sampled_signal(end);

sinc_signal = zeros(size(reference_time));

for sample_index = 1:length(sample_time)
    normalized_distance = (reference_time - sample_time(sample_index)) / sample_interval;
    sinc_signal = sinc_signal + sampled_signal(sample_index) .* sinc(normalized_distance);
end

number_of_samples = length(sampled_signal);
complex_spectrum = fft(sampled_signal);
positive_count = floor(number_of_samples / 2) + 1;

amplitude_spectrum = abs(complex_spectrum(1:positive_count)) / number_of_samples;
amplitude_spectrum(2:end - 1) = 2 * amplitude_spectrum(2:end - 1);

frequency_bins = (0:(positive_count - 1)) * sample_rate / number_of_samples;

[maximum_amplitude, dominant_index] = max(amplitude_spectrum);
dominant_frequency = frequency_bins(dominant_index);

zoh_rmse = sqrt(mean((reference_signal - zoh_signal).^2));
linear_rmse = sqrt(mean((reference_signal - linear_signal).^2));
sinc_rmse = sqrt(mean((reference_signal - sinc_signal).^2));

fprintf("MATLAB validation - safe sampling\n");
fprintf("Original frequency: %.1f Hz\n", signal_frequency);
fprintf("Sampling frequency: %.1f Hz\n", sample_rate);
fprintf("Dominant frequency: %.1f Hz\n", dominant_frequency);
fprintf("Maximum FFT amplitude: %.6f\n", maximum_amplitude);
fprintf("ZOH RMSE: %.6f\n", zoh_rmse);
fprintf("Linear RMSE: %.6f\n", linear_rmse);
fprintf("Sinc RMSE: %.6f\n", sinc_rmse);

figure;

subplot(3, 1, 1);
plot(reference_time, reference_signal, "k", "LineWidth", 1.5);
hold on;
plot(sample_time, sampled_signal, "bo", "MarkerFaceColor", "b");
grid on;
title("Original Signal and Samples");
xlabel("Time [s]");
ylabel("Amplitude");
legend("Original", "Samples");

subplot(3, 1, 2);
stem(frequency_bins, amplitude_spectrum, "filled");
grid on;
title("Normalized Sample Spectrum");
xlabel("Frequency [Hz]");
ylabel("Amplitude");

subplot(3, 1, 3);
plot(reference_time, reference_signal, "k", "LineWidth", 1.5);
hold on;
plot(reference_time, zoh_signal, "r");
plot(reference_time, linear_signal, "g");
plot(reference_time, sinc_signal, "m");
grid on;
title("Reconstruction Comparison");
xlabel("Time [s]");
ylabel("Amplitude");
legend("Original", "ZOH", "Linear", "Sinc");
