numerator = [9];
denominator = [1 2 10];
system_model = tf(numerator, denominator);
disp("MATLAB transfer function:")
disp(system_model)
system_poles = pole(system_model);
system_zeros = zero(system_model);
disp("Poles:")
disp(system_poles)
disp("Zeros:")
disp(system_zeros)
time_values = linspace(0, 8, 801);
[step_response, step_time] = step(system_model, time_values);
[impulse_response, impulse_time] = impulse(system_model, time_values);
step_response = squeeze(step_response);
impulse_response = squeeze(impulse_response);
fprintf("\nControlled time grid\n")
fprintf("Number of points: %d\n", length(time_values))
fprintf("Start time: %.1f\n", time_values(1))
fprintf("End time: %.1f\n", time_values(end))
fprintf("\nSelected step-response values\n")
fprintf("t = 0 s: %.15f\n", step_response(1))
fprintf("t = 1 s: %.15f\n", step_response(101))
fprintf("t = 2 s: %.15f\n", step_response(201))
fprintf("t = 8 s: %.15f\n", step_response(801))
fprintf("\nSelected impulse-response values\n")
fprintf("t = 0 s: %.15f\n", impulse_response(1))
fprintf("t = 1 s: %.15f\n", impulse_response(101))
fprintf("t = 2 s: %.15f\n", impulse_response(201))
fprintf("t = 8 s: %.15f\n", impulse_response(801))
figure
subplot(2, 1, 1)
plot(step_time, step_response)
yline(0.9, "--", "DC gain = 0.9")
title("MATLAB Step Response")
xlabel("Time [s]")
ylabel("y(t)")
grid on
subplot(2, 1, 2)
plot(impulse_time, impulse_response)
title("MATLAB Impulse Response")
xlabel("Time [s]")
ylabel("h(t)")
grid on