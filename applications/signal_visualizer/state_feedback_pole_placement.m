A = [0 1; -2 -3];
B = [0; 1];
p = [-4 -5];
p_slow = [-2 -3];
p_fast = [-10 -12];
x0 = [1; 0];

K = place(A, B, p)
K_slow = place(A, B, p_slow)
K_fast = place(A, B, p_fast)

u_slow = -K_slow*x0
u_fast = -K_fast*x0

closed_loop = A - B*K
poles = eig(closed_loop)
[V D] = eig(closed_loop)