plant = tf([2], [5 1]);
controller = tf([4], [1]);
open_loop = series(controller, plant)
closed_loop = feedback(open_loop, 1)
step(closed_loop)
