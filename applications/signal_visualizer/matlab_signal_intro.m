% MATLAB signal introduction
t = 0:0.01:1;
f = 2;
x = sin(2*pi*f*t);
plot(t, x)
xlabel("Time [s]")
ylabel("Amplitude")
title("2 Hz Sine Wave")
grid on
