import numpy as np
from sympy import symbols, diff, Poly


def lerp(p0, p1, t):
    return (1-t)*p0 + t*p1


def bezier(p0, p1, p2, p3, t):
    l0 = lerp(p0, p1, t)
    l1 = lerp(p1, p2, t)
    l2 = lerp(p2, p3, t)
    l3 = lerp(l0, l1, t)
    l4 = lerp(l1, l2, t)
    l5 = lerp(l3, l4, t)
    return l5


def distance(p0, p1):
    return np.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)


x0, y0, x1, y1, x2, y2, x3, y3 = symbols('x0 y0 x1 y1 x2 y2 x3 y3')

points = [(2, 3),
          (4, 4),
          (3, 2.5),
          (4.5, 5)
          ]


def f(x0, y0, x1, y1, x2, y2, x3, y3):
    _sum = 0
    for t, (x, y) in enumerate(points):
        _sum += distance(bezier(x0, x1, x2, x3, t), (x, y))


dx0 = Poly(diff(f(x0, y0, x1, y1, x2, y2, x3, y3), x0)).coeffs()
dy0 = Poly(diff(f(x0, y0, x1, y1, x2, y2, x3, y3), y0)).coeffs()
dx1 = Poly(diff(f(x0, y0, x1, y1, x2, y2, x3, y3), x1)).coeffs()
dy1 = Poly(diff(f(x0, y0, x1, y1, x2, y2, x3, y3), y1)).coeffs()
dx2 = Poly(diff(f(x0, y0, x1, y1, x2, y2, x3, y3), x2)).coeffs()
dy2 = Poly(diff(f(x0, y0, x1, y1, x2, y2, x3, y3), y2)).coeffs()
dx3 = Poly(diff(f(x0, y0, x1, y1, x2, y2, x3, y3), x3)).coeffs()
dy3 = Poly(diff(f(x0, y0, x1, y1, x2, y2, x3, y3), y3)).coeffs()

A = np.array([dx0[:-1], dy0[:-1], dx1[:-1], dy1[:-1], dx2[:-1], dy2[:-1], dx3[:-1], dy3[:-1]], dtype=float)

X = np.linalg.solve(A, B).flatten()

print(f'y^ = {round(X[1], 3)}x + {round(X[0], 3)}')
