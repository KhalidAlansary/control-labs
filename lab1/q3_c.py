import sympy as sp

t, s = sp.symbols("t s")

x3 = sp.exp(-0.3 * t) * sp.sin(3 * t)
X3 = sp.laplace_transform(x3, t, s)[0]
print("X3 = \n")
sp.pretty_print(X3)
