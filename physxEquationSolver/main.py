import os
import time
import numpy as np
from sympy import nonlinsolve
from sympy.parsing.sympy_parser import parse_expr

def permutate(arr,available):
    out = []
    solveFor = []
    bad = [" ", "*", "/", "+", "-", "(", ")"]
    for char in available:
        if findVar(arr[0],char,bad) or findVar(arr[1],char,bad):
            solveFor.append(char)
    for char in solveFor:
        print("Solving",arr,"for",char)
        yeeet = list(iter(nonlinsolve([parse_expr("-".join([arr[1],arr[0]]))],(parse_expr(char)))))
        print(yeeet)
        print(len(yeeet))

        try:
            while len(yeeet) == 1:
                yeeet = list(iter(yeeet[0]))
            raise
        except:
            try:
                while len(yeeet) > 1:
                    yeeet = yeeet[0]
            except:
                pass


        print(yeeet)
        for i in yeeet:
            temp = str(i)
            temp = temp.replace(",","")
            out.append([char,temp])
            print([char,temp])
        # final = [char,list(nonlinsolve([parse_expr("-".join([arr[1],arr[0]]))],(parse_expr(char))))[0][0]]

        # print(final)
        # out.append(final)

    return out

def generator(equations,available):
    output = []
    temp = []
    # print("before:",equations)
    for arr in equations:
        temp.extend(permutate(arr,available))
        for d in range(len(temp)-1,-1,-1):
            for eq in range(len(equations)-1,-1,-1):
                if equations[eq][0] == temp[d][0] and equations[eq][1] == temp[d][1]:
                    temp.pop(d)
                    d-=1
    equations.extend(temp)
    # print("after:",equations)

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
                    if "complexes" in garit[1].lower() or "emptyset" in garit[1].lower() or "conditionset" in garit[1].lower():
                        break
                else:
                    garit = [equations[loc[m]][1],equations[loc[m+1]][1]]
                output.append(garit)
                # print(equations)
    temp = []
    # print("before:",equations)
    for arr in output:
        temp.extend(permutate(arr,available))
        # print("temp:",temp)
        for d in range(len(temp)-1,-1,-1):
            for eq in range(len(output)-1,-1,-1):
                # print(d)
                if output[eq][0] == temp[d][0] and output[eq][1] == temp[d][1]:
                    # print("pop!")
                    temp.pop(d)
                    # print(temp)
                    d-=1
    equations.extend(temp)
    # print("after:",equations)
    equations.reverse()
    # print(equations)
    for i in range(len(equations)-1,-1,-1):
        # print("testing 0:",equations[i])
        if equations[i][1] == "0":
            # print("0:",equations[i])
            equations.pop(i)
    return equations

def replaceExclude(string, name, val, bad):

    # print("before:",string)
    out = string
    length = len(name)
    i = 0
    while i < len(string)-length+1:
        # print(string[i:i+length])
        if string[i:i+length] == name:
            isLeftGood = False
            isRightGood = False
            if i != 0:
                if string[i-1] in bad:
                    isLeftGood = True
            else: isLeftGood = True
            if i != len(string)-length:
                if string[i+length] in bad:
                    isRightGood = True
            else: isRightGood = True
            if isLeftGood and isRightGood:
                # print("Replacing",name,"with",val,"in",string)
                out = out[:i]+val+out[i+length:]
                i += len(val)
            # print(string[i:i+length],isLeftGood,isRightGood)
        i += 1
    # print("after:",out)

    return out

def findVar(string, name, bad):

    # print("before:",string)
    length = len(name)
    i = 0
    while i < len(string)-length+1:
        # print(string[i:i+length])
        if string[i:i+length] == name:
            isLeftGood = False
            isRightGood = False
            if i != 0:
                if string[i-1] in bad:
                    isLeftGood = True
            else: isLeftGood = True
            if i != len(string)-length:
                if string[i+length] in bad:
                    isRightGood = True
            else: isRightGood = True
            if isLeftGood and isRightGood:
                # print("Replacing",name,"with",val,"in",string)
                return True
            # print(string[i:i+length],isLeftGood,isRightGood)
        i += 1
    # print("after:",out)

    return False
"""
t = theta*5
"""

"""
1. Scan all equations for "var = val" X
2. Evaluate var X
3. replace var with val in all right sides of equations X
4. remove "var = val" from list. X
5. repeat X
"""
def gigaMegaSolver(equations,formulas,available,bad,done=[]):
    i = -1
    while -i < len(equations):
        if len(equations) == 0 or len(formulas) == 0:
            return
        # ====================
        # Test for any variables in right side of equation.
        n = 0
        # print(equations[i][1])
        # print(looking)
        for k in available:
            if k in equations[i][1]:
                n += 1
        # ====================
        # If none, solve variable equal to expression.
        if n == 0:
            val = str(eval(equations[i][1])) # Evaluate
            name = equations[i][0]
            if name in available: # If variable being solved for was not provided in beginning.
                # print("eq:",equations)
                # print("form:",formulas)
                print("Using equation:",formulas[i][0],"=",formulas[i][1])
                print("Plugging in values:",equations[i][0],"=",equations[i][1])
             # Change known variable to solved variable for next iteration.
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
                    equations[j][1] = replaceExclude(equations[j][1],name,val,bad)
            # Recurse
            gigaMegaSolver(equations,formulas,available,bad,done)
        i -= 1

def build(equationsFileName,constantsFileName,outputName):
    f = open(equationsFileName, "r")
    temp = f.readlines()
    equations = [i[:-1].split(" = ") for i in temp]

    f.close()
    temp = " ".join(np.asarray(equations).flatten())

    bad = [" ", "*", "/", "+", "-", "(", ")"]
    remove = ["sin", "cos", "sqrt"]
    available = []
    i = 0
    while i < len(temp):
        for j in range(i+1,len(temp)):
            if temp[i] not in bad and temp[j] in bad:
                # print(temp[i:j])
                available.append(temp[i:j])
                i += len(temp[i:j])
                break
            if temp[j] in bad:
                break
        i += 1

    available = list(dict.fromkeys(available))
    thing = list(available)
    thing.reverse()
    for char in thing:
        try:
            float(char)
            available.remove(char)
        except:
            for removeChar in remove:
                if removeChar in char:
                    available.remove(char)

    f = open(constantsFileName, "r")
    arr = [i[:-1].split(" = ") for i in f.readlines()]
    f.close()

    for c in arr:
        if c[0] in available:
            available.remove(c[0])

    print("Permutating...")

    yes = generator(equations,available)

    for e in yes:
        for c in arr:
            e[1] = replaceExclude(e[1],c[0],c[1],bad)
            e[0] = replaceExclude(e[0],c[0],c[1],bad)

    os.system("md "+outputName)
    np.save(outputName+"/bad",bad)
    np.save(outputName+"/arr",arr)
    np.save(outputName+"/permutated",yes)
    np.save(outputName+"/available",available)
    print("Done.")

def run(directory):
    bad = np.load(directory+"/bad.npy").tolist()
    arr = np.load(directory+"/arr.npy").tolist()
    available = np.load(directory+"/available.npy").tolist()
    print("Available variables:",available)

    while True:
        stuff = input("var name? ")
        if stuff == "end":
            break
        if stuff not in available:
            print("Variable is not available for evaluation.")
            continue
        know = stuff
        val = input(know+" = ")
        arr.append([know,val])

    # os.system('cls')
    equations2 = np.load(directory+"/permutated.npy").tolist()
    formulas2 = np.load(directory+"/permutated.npy").tolist().copy()

    for e in equations2:
        for c in arr:
            e[1] = replaceExclude(e[1],c[0],c[1],bad)
            e[0] = replaceExclude(e[0],c[0],c[1],bad)

    gigaMegaSolver(equations2,formulas2,available,bad)
