import numpy as np
from sympy import symbols, diff, Poly

m, b = symbols('m b')

points = [(2, 3),
          (4, 4),
          (3, 2.5),
          (4.5, 5)
]

f = lambda m, b: sum([(y-(x*m+b))**2 for x, y in points])

mC = Poly(diff(f(m, b), m)).coeffs()
bC = Poly(diff(f(m, b), b)).coeffs()

A = np.array([mC[:-1], bC[:-1]], dtype=float)
B = np.array([[-mC[-1]], [-bC[-1]]], dtype=float)

X = np.linalg.solve(A, B).flatten()

print(f'y^ = {round(X[1], 3)}x + {round(X[0], 3)}')
