plant = tf([2], [5 1]);
Kp = 2;
Ki = 2;
Kd = 2;
P_regulator = Kp;
open_loop = series(P_regulator, plant);
closed_loop = feedback(open_loop, 1);
s = tf([1 0], [1])
PI_regulator = Kp + Ki/s;
openLoopPI = series(PI_regulator, plant);
closedLoopPI = feedback(openLoopPI, 1);
PID_regulator = Kp + Ki/s + Kd*s;
openLoopPID = series(PID_regulator, plant);
closedLoopPID = feedback(openLoopPID, 1);
step(closed_loop, closedLoopPI, closedLoopPID)
legend("P", "PI", "PID")
grid on
