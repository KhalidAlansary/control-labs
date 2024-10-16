from scipy.signal import residue

num = [2, 5, 3, 6]
den = [1, 6, 11, 6]

r, p, k = residue(num, den)

print("r = ", r)
print("p = ", p)
print("k = ", k)
