A = [-1 0; 0 -2];
B = [1; 1];
C = [1 0];

controlability = ctrb(A, B)
observability = obsv(A, C)
ctrb_rank = rank(controlability)
obsv_rank = rank(observability)