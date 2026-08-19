t = linspace(-3, 3, 3001);
frequencies = linspace(-10, 10, 3001);
tau_values = [0.25 0.5 1 2];

for i = 1:length(tau_values)
    tau = tau_values(i);

    x = abs(t) <= tau / 2;
    X = tau * sinc(frequencies * tau);
    bandwidth = 1 / tau;

    subplot(4, 2, 2*i - 1)
    plot(t, x)
    grid on
    ylabel("Amplitude")
    title(sprintf("Pulse width = %g s", tau))

    subplot(4, 2, 2*i)
    plot(frequencies, X)
    grid on
    ylabel("Amplitude")
    title(sprintf("Bandwidth = %g Hz", bandwidth))

    xline(bandwidth, "r")
    xline(-bandwidth, "r")

    if i == length(tau_values)
        subplot(4, 2, 2*i - 1)
        xlabel("Time [s]")

        subplot(4, 2, 2*i)
        xlabel("Frequency [Hz]")
    end
end
