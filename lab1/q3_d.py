import sympy as sp

t, s = sp.symbols("t s")

x4 = sp.exp(0.1 * t) * sp.sin(3 * t)
X4 = sp.laplace_transform(x4, t, s)[0]
print("X4 = \n")
sp.pretty_print(X4)
