import numpy as np

import control as ct

A = [
    [0, 1],
    [-25, -4],
]
B = [
    [1, 1],
    [0, 1],
]
C = [
    [1, 0],
    [0, 1],
]
D = [
    [0, 0],
    [0, 0],
]

sys = ct.ss2tf(A, B, C, D, 1)
# clean up and approximate the coefficients
sys.num[1][0] = np.round(sys.num[1][0], 2)
print(sys)
sys = ct.ss2tf(A, B, C, D, 2)
sys.num[1][0] = np.round(sys.num[1][0], 2)
print(sys)
