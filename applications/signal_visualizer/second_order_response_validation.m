clear;
clc;
close all;

natural_frequency = 5.0;
input_value = 1.0;
damping_ratios = [0.0, 0.2, 1.0, 2.0];

evaluation_times = linspace(0.0, 8.0, 1601);
initial_state = [0.0; 0.0];

responses = zeros(length(evaluation_times), length(damping_ratios));

figure_handle = figure("Position", [100, 100, 1400, 500]);
tiledlayout(1, 2);

nexttile;
hold on;

solver_options = odeset("RelTol", 1e-9, "AbsTol", 1e-12);

for index = 1:length(damping_ratios)
    damping_ratio = damping_ratios(index);

    derivative = @(time, state) [
        state(2);
        natural_frequency^2 * (input_value - state(1)) ...
        - 2.0 * damping_ratio * natural_frequency * state(2)
    ];

    [times, states] = ode45(derivative, evaluation_times, initial_state, solver_options);

    responses(:, index) = states(:, 1);

    plot(times, states(:, 1), "LineWidth", 1.5, ...
        "DisplayName", sprintf("\\zeta = %.1f", damping_ratio));
end

yline(input_value, "k--", "Target");
title("Step responses");
xlabel("Time [s]");
ylabel("Output y(t)");
grid on;
legend("Location", "best");
hold off;

resonance_damping_ratios = [0.2, 1.0, 2.0];
frequency_ratios = logspace(-1.0, 1.0, 1200);

nexttile;
hold on;

for index = 1:length(resonance_damping_ratios)
    damping_ratio = resonance_damping_ratios(index);

    magnitude = 1.0 ./ sqrt( ...
        (1.0 - frequency_ratios.^2).^2 ...
        + (2.0 * damping_ratio * frequency_ratios).^2 ...
    );

    semilogx(frequency_ratios, magnitude, "LineWidth", 1.5, ...
        "DisplayName", sprintf("\\zeta = %.1f", damping_ratio));
end

xline(1.0, "k--", "Natural frequency");
title("Resonance and damping");
xlabel("Frequency ratio \omega / \omega_n");
ylabel("Magnitude");
ylim([0.0, 3.0]);
grid on;
legend("Location", "best");
hold off;

checked_index = find(damping_ratios == 0.2, 1);
checked_output = responses(:, checked_index);

[numerical_peak, peak_index] = max(checked_output);
numerical_peak_time = evaluation_times(peak_index);
numerical_overshoot = (numerical_peak - input_value) / input_value * 100.0;

theoretical_overshoot = exp( ...
    -0.2 * pi / sqrt(1.0 - 0.2^2) ...
) * 100.0;

checked_magnitude = 1.0 ./ sqrt( ...
    (1.0 - frequency_ratios.^2).^2 ...
    + (2.0 * 0.2 * frequency_ratios).^2 ...
);

[maximum_magnitude, resonance_index] = max(checked_magnitude);
numerical_resonance_frequency = frequency_ratios(resonance_index) * natural_frequency;
theoretical_resonance_frequency = natural_frequency * sqrt(1.0 - 2.0 * 0.2^2);

assert(abs(numerical_overshoot - theoretical_overshoot) < 0.1);
assert(abs(numerical_resonance_frequency - theoretical_resonance_frequency) < 0.02);

fprintf("MATLAB VALIDATION\n\n");
fprintf("Numerical peak: %.9f\n", numerical_peak);
fprintf("Numerical peak time: %.6f s\n", numerical_peak_time);
fprintf("Numerical overshoot: %.9f %%\n", numerical_overshoot);
fprintf("Theoretical overshoot: %.9f %%\n", theoretical_overshoot);
fprintf("Overshoot difference: %.9f %%\n", abs(numerical_overshoot - theoretical_overshoot));
fprintf("Numerical resonance frequency: %.9f rad/s\n", numerical_resonance_frequency);
fprintf("Theoretical resonance frequency: %.9f rad/s\n", theoretical_resonance_frequency);
fprintf("Maximum resonance magnitude: %.9f\n", maximum_magnitude);
fprintf("\nMATLAB checks passed.\n");

exportgraphics(figure_handle, "second_order_response_validation.png", "Resolution", 180);
