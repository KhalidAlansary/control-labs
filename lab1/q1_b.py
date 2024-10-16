import numpy as np
from scipy.signal import residue

num = [1, 2, 3]
den = [1, 3, 3, 1]

r, p, k = residue(num, den)

# Round or clean up residues and poles
r = np.real_if_close(r.round(2))
p = np.real_if_close(p.round(2))

print("r = ", r)
print("p = ", p)
print("k = ", k)
