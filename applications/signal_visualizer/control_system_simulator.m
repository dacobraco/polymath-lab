m = 1;
b = 2;
k = 10;
plant = tf([1], [m, b, k]);

A = [0 1; -k/m -b/m];
B = [0; 1/m];
C = [1 0];
D = [0];

system = ss(A, B, C, D);
Kp = 10;
Ki = 5;
Kd = 3;
open_loop = Kp * plant;
closed_loop = feedback(open_loop, 1);

s = tf([1 0], [1]);
PI_controller = Kp + Ki/s;
open_loop_PI = PI_controller * plant;
closed_loop_PI = feedback(open_loop_PI, 1);

PID_controller = Kp + Ki/s + Kd*s;
open_loop_PID = PID_controller * plant;
closed_loop_PID = feedback(open_loop_PID, 1);

K = place(A, B, [-4 -5]);
A_closed = A - B*K;
Nr = -1 / (C * inv(A - B*K) * B);
state_system = ss(A_closed, B*Nr, C, D);
step(closed_loop, closed_loop_PI, closed_loop_PID, state_system)
grid on
title("Control System Simulator")
legend("P", "PI", "PID", "State Feedback")

P_info = stepinfo(closed_loop)
PI_info = stepinfo(closed_loop_PI)
PID_info = stepinfo(closed_loop_PID)
StateFeedback_info = stepinfo(state_system)
