A = [0 1; -2 -3];
B = [0; 1];
C = [1 0];
D = [0];
K = [18 6];

Nr = -1 / (C * inv(A - B*K) * B);

Acl = A - B*K;

system_without_Nr = ss(Acl, B, C, D);
system_with_Nr = ss(Acl, B*Nr, C, D);

figure;
step(system_without_Nr, system_with_Nr);
grid on;
legend("Without Nr", "With Nr");
yline(1, "--", "Reference");
title("State Feedback Reference Tracking");
xlabel("Time (s)");
ylabel("Output");