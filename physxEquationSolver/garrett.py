import os
import time
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

def permutate(arr,available):
    out = []
    solveFor = []
    for char in available:
        if char in arr[0] or char in arr[1]:
            solveFor.append(char)
    for char in solveFor:
        out.append([char,str(list(nonlinsolve([parse_expr("-".join([arr[1],arr[0]]))],(parse_expr(char))))[0][0]])
    return out    
