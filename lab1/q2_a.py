import control as ct

num1 = [10]
den1 = [1, 2, 10]
num2 = [5]
den2 = [1, 5]

G1 = ct.tf(num1, den1)
G2 = ct.tf(num2, den2)

G_series = ct.series(G1, G2)
print(G_series)

G_parallel = ct.parallel(G1, G2)
print(G_parallel)

G_feedback = ct.feedback(G1, G2)
print(G_feedback)
