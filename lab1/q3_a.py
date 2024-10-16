import sympy as sp

t, s, a = sp.symbols("t s a")

x1 = t**2 * sp.exp(-a * t) + 3 * t
X1 = sp.laplace_transform(x1, t, s)[0]
print("X1 = \n")
sp.pretty_print(X1)
