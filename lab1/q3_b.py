import sympy as sp

t, s = sp.symbols("t s")

x2 = sp.exp(-0.1 * t) * sp.sin(3 * t)
X2 = sp.laplace_transform(x2, t, s)[0]
print("X2 = \n")
sp.pretty_print(X2)
