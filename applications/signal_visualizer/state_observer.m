A = [0 1; -2 -3];
C = [1 0];
observer_poles = [-5 -6];
z = [1; 1; 0; 0];
time = 0:0.01:5;

poles = eig(A);
L = place(A', C', observer_poles)';
eig(A - L*C);

A_aug = [A zeros(2); L*C A-L*C];
B_aug = zeros(4,1);
C_aug = eye(4);
D_aug = zeros(4,1);

observer_system = ss(A_aug, B_aug, C_aug, D_aug);
[y, t] = initial(observer_system, z, time);
y(end,:)

figure
plot(t, y(:,1), 'LineWidth', 2)
hold on
plot(t, y(:,3), 'LineWidth', 2)
grid on
xlabel('Time (s)')
ylabel('State value')
title('State x1: actual vs estimated')
legend('x1 actual', 'x1 estimated')

figure
plot(t, y(:,2), 'LineWidth', 2)
hold on
plot(t, y(:,4), 'LineWidth', 2)
grid on
xlabel('Time (s)')
ylabel('State value')
title('State x2: actual vs estimated')
legend('x2 actual', 'x2 estimated')