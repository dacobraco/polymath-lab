plant = tf([1], [1 6 5 0]);
Kp = 18;
Ki = 12.81;
Kd = 10;
s = tf([1 0], [1]);
PID_regulator = Kp + Ki/s + Kd*s;
open_loop = series(PID_regulator, plant);
closed_loop = feedback(open_loop, 1);
info = stepinfo(closed_loop)
step(closed_loop)
isstable(closed_loop)
grid on
