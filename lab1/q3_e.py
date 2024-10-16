import sympy as sp

t, s = sp.symbols("t s")

x5 = sp.exp(0.3 * t) * sp.sin(3 * t)
X5 = sp.laplace_transform(x5, t, s)[0]
print("X5 = \n")
sp.pretty_print(X5)
