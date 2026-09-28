import control
import matplotlib.pyplot as plt

plant = control.tf([10], [1, 7, 10, 0])

control.bode_plot(plant, display_margins=True)
plt.show()

gm, pm, wcg, wcp = control.margin(plant)

print("GM:", gm)
print("PM:", pm)
print("WcG:", wcg)
print("WcP:", wcp)

control.nyquist_plot(plant)
plt.show()

open_loop_K3 = 3 * plant
closed_loop_K3 = control.feedback(open_loop_K3, 1)

open_loop_K7 = 7 * plant
closed_loop_K7 = control.feedback(open_loop_K7, 1)

open_loop_K8 = 8 * plant
closed_loop_K8 = control.feedback(open_loop_K8, 1)

t3, y3 = control.step_response(closed_loop_K3)
t7, y7 = control.step_response(closed_loop_K7)
t8, y8 = control.step_response(closed_loop_K8)

plt.figure()
plt.plot(t3, y3)
plt.title("K = 3")
plt.grid()

plt.figure()
plt.plot(t7, y7)
plt.title("K = 7")
plt.grid()

plt.figure()
plt.plot(t8, y8)
plt.title("K = 8")
plt.grid()

plt.figure()

control.nyquist_plot(3 * plant, label="K=3")
control.nyquist_plot(7 * plant, label="K=7")
control.nyquist_plot(8 * plant, label="K=8")

plt.xlim([-2, 0.5])
plt.ylim([-1.5, 1.5])
plt.grid()
plt.legend()
plt.show()
