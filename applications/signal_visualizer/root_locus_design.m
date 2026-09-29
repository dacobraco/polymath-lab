plant = tf([10], [1 7 10 0]);
rlocus(plant);
grid on
title("Root Locus of G(s)")
[K, poles] = rlocfind(plant)
controller = K;
closed_loop = feedback(controller * plant, 1);

figure
step(closed_loop)
grid on
title("Closed-Loop Response for Root Locus Gain")

info = stepinfo(closed_loop)