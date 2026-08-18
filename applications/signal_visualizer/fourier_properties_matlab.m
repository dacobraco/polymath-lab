function X = numerical_fourier_transform(t, x, frequencies)

X = zeros(size(frequencies));

for i = 1:length(frequencies)
    f = frequencies(i);

    exponent = - 1j * 2 * pi * f * t;
    integrand = x .* exp(exponent);
    X(i) = trapz(t, integrand);
end

end

t = linspace(-5, 5, 5001);
f = linspace(-5, 5, 501);
x1 = exp(-pi * t.^2);
x2 = exp(-2 * pi * t.^2);
y = 2 * x1 - 3 * x2;

X1 = numerical_fourier_transform(t, x1, f);
X2 = numerical_fourier_transform(t, x2, f);
Y_direct = numerical_fourier_transform(t, y, f);
Y_linear = 2 * X1 - 3 * X2;

linearity_error = max(abs(Y_direct - Y_linear))

x_dual = exp(-pi * (t - 1).^2);
X_dual = numerical_fourier_transform(t, x_dual, f);
XX_dual = numerical_fourier_transform(f, X_dual, t);
x_reflected = exp(-pi * (t + 1).^2);

duality_error = max(abs(XX_dual - x_reflected))
