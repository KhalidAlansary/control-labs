import sympy as sp
from q3_b import x2
from q3_c import x3

sp.plot(
    x2,
    x3,
    (sp.symbols("t"), 0, 10),
    title="x2(t) and x3(t)",
    xlabel="t",
    ylabel="x(t)",
)
