import control as ct

A = [
    [0, 1, 0],
    [0, 0, 1],
    [-5, -25, -5],
]
B = [
    [0],
    [25],
    [-120],
]
C = [1, 0, 0]
D = [0]

sys = ct.ss2tf(A, B, C, D)
num = sys.num[0][0]
den = sys.den[0][0]

print(sys)
print("num = \n", num)
print("den = \n", den)
