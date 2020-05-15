import os
import time
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

equations = [["a","v/t"], ["F","m*a"], ["v","d/t"], ["W", "F*d"], ["W", "P*t"]]

formulas =  [["a","v/t"], ["F","m*a"], ["v","d/t"], ["W", "F*d"], ["W", "P*t"]]

# from converter import convert
# equations = convert()
# formulas = convert()

def permutate(arr,available):
    out = []
    solveFor = []
    for char in available:
        if char in arr[0] or char in arr[1]:
            solveFor.append(char)
    for char in solveFor:
        # print("Solving",arr,"for",char)
        final = [char,list(nonlinsolve([parse_expr("-".join([arr[1],arr[0]]))],(parse_expr(char))))[0][0]]
        final[1] = str(final[1])
        if "complexes" in final[1].lower():
            break
        if "complement" in final[1].lower():
            n = 0
            for i in range(len(final[1])):
                if final[1][i] == "(" and n < 2:
                    n += 1
                    start = i+1
                if final[1][i] == ")":
                    end = i
                    break
            final[1] = final[1][start:end]
            if "(" in final[1]:
                final[1] = final[1]+")"
        # print(final)
        out.append(final)
    return out

def generator(equations,available):
    output = []
    temp = []
    for arr in equations:
        temp.extend(permutate(arr,available))
    equations.extend(temp)
    for p in equations:
        loc = []
        for l in range(len(equations)):
            if equations[l][0] == p[0] and [equations[l][1],p[1]] not in output:
                if equations[l][0] in available and p[0] in available:
                    loc.append(l)
        for m in range(len(loc)-1):
            if [equations[loc[m]][1],equations[loc[m+1]][1]] not in output:
                numVars = 0
                for k in available:
                    if k in equations[loc[m]][1]+equations[loc[m+1]][1]:
                        solveFor = k
                        numVars+=1
                if numVars == 1:
                    garit = [k,str(list(nonlinsolve([" - ".join([equations[loc[m]][1],equations[loc[m+1]][1]])],(parse_expr(solveFor))))[0][0])]
                else:
                    garit = [equations[loc[m]][1],equations[loc[m+1]][1]]
                output.append(garit)
                # print(equations)
    temp = []
    for arr in output:
        temp.extend(permutate(arr,available))
    equations.extend(temp)
    equations.reverse()
    # print(equations)
    return equations

"""
1. Scan all equations for "var = val" X
2. Evaluate var X
3. replace var with val in all right sides of equations X
4. remove "var = val" from list. X
5. repeat X
"""
def gigaMegaSolver(equations,formulas,available,done=[]):
    i = -1
    while -i < len(equations):
        if len(equations) == 0 or len(formulas) == 0:
            return
        # ====================
        # Test for any variables in right side of equation.
        n = 0
        # print(equations[i][1])
        for j in equations[i][1]:
            for k in available:
                if k in j and "sqrt" not in equations[i][1]: # ''"sqrt" not in' is a temp fix
                    n += 1
        # ====================
        # If none, solve variable equal to expression.
        if n == 0:
            if formulas[i][0] not in initial: # If variable being solved for was not provided in beginning.
                print("Using equation:",formulas[i][0],"=",formulas[i][1])
                print("Plugging in values:",equations[i][0],"=",equations[i][1])
            val = str(eval(equations[i][1])) # Evaluate
            name = equations[i][0] # Change known variable to solved variable for next iteration.
            print(name,"=",val)
            done.append(name) # Add solved variable to list of solved variables.
            # ====================
            # Remove all occasions of "newly solved variable = something".
            for j in range(len(equations)-1,-1,-1):
                if equations[j][0] in done:
                    equations.pop(j)
                    formulas.pop(j)
                elif name in equations[j][1]:
                    # Replace all occasions of newly solved variable with value.
                    equations[j][1] = equations[j][1].replace(name,val)
            # Recurse
            gigaMegaSolver(equations,formulas,available,done)
        i -= 1

f = open("equations.txt", "r")
equations = [i[:-1].split(" = ") for i in f.readlines()]
formulas = [i[:-1].split(" = ") for i in f.readlines()]
# print(equations)

tempList = []

for i in equations:
    try:
        i.split("*")
        break
    except:
        pass
    try:
        i.split

available = list(dict.fromkeys(tempList))
print("Available variables:",available)

initial = []

while True:
    stuff = input("var name? ")
    if stuff == "end":
        break
    know = stuff
    val = input(know+" = ")
    initial.append(know)
    equations.append([know,val])
    formulas.append([know,val])

os.system('cls')
equations2 = generator(equations,available)
formulas2 = generator(formulas,available)

gigaMegaSolver(equations2,formulas2,available)
