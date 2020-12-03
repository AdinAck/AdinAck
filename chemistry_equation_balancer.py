import numpy as np
from sympy import *

components = [[],[]]
# components = [['Fe', 'O2'], ['Fe3 O4']]
# components = [['C H4', 'O2'], ['C O2', 'H2 O']]
# components = [['Ba Cl2', 'H2 S O4'], ['Ba S O4', 'H Cl']]
components = [['Fe S2', 'O2'], ['Fe2 O3', 'S O2']]
# components = [['Fe2 O3', 'H2'], ['Fe', 'H2 O']]
# components = [['N Br3', 'Na O H'],['N2', 'Na Br', 'H O Br']]
# components = [['Al', 'Cu S O4'], ['Al2 S3 O12', 'Cu']]
# components = [['Al O3 H3', 'H2 S O4'], ['Al2 S3 O12', 'H2 O']]
# components = [['K4 Fe C6 N6', 'K Mn O4', 'H2 S O4'],['K H S O4', 'Fe2 S3 O12', 'Mn S O4', 'H N O3', 'C O2', 'H2 O']]
# components = [['C5 H8 O2', 'Na H', 'H Cl'], ['C5 H12 O2', 'Na Cl']]
# components = [['C7 H9', 'H N O3'], ['C7 H6 N3 O6', 'H2 O']]
# components = [['C H4', 'H2 O'], ['H2', 'C O']]

# for i in range(2):
#     val = ""
#     print("Components:")
#     while val != "end":
#         val = input()
#         if val != "end":
#             components[i].append(val)
# print(components)

componentsDict = [[],[]]
for _ in range(len(components[0])):
    componentsDict[0].append({})

for _ in range(len(components[1])):
    componentsDict[1].append({})

for i in range(len(components)):
    for j in range(len(components[i])):
        for k in components[i][j].split(" "):
            tmp = -1
            for char in range(len(k)-1,-1,-1):
                if k[char].isdigit():
                    tmp = char
            if tmp != -1:
                componentsDict[i][j][k[:tmp]] = k[tmp:]
            else:
                componentsDict[i][j][k] = "1"

# print the dicts of elements
# print()
# for i in componentsDict:
#     for j in i:
#         print(j)
#     print()

# make list of elements to be counted
alphabet = []
for i in componentsDict[0]:
    alphabet.extend(i.keys())

alphabet = list(dict.fromkeys(alphabet))

# print(alphabet)

matrix = np.zeros((len(alphabet),len(components[0])+len(components[1])))

lut = {}
for i in range(len(alphabet)-1,-1,-1):
    lut[alphabet[i]] = i

# print('lut')
# print(lut)

for i in range(len(componentsDict)):
    for j in range(len(componentsDict[i])):
        for e,v in componentsDict[i][j].items():
            # print(i,j,e,v)
            matrix[lut[e],j+i*len(componentsDict[0])] = v

# print(componentsDict)

m1 = matrix[:,:len(componentsDict[0])]
m2 = matrix[:,len(componentsDict[0]):]
m2 = -m2
# print(m1)
# print(m2)

matrix = np.concatenate((m1,m2), axis=1)

ns = [i[0] for i in np.array(Matrix([[int(j) for j in list(i)] for i in matrix]).nullspace())[0]]

denominator = max([i[1] for i in [fraction(j) for j in ns] if i[1] != 1])

coeffs = [j * denominator for j in ns]
ca = coeffs[:len(componentsDict[0])],coeffs[len(componentsDict[0]):]

print("\n/////////////////////////\n")
print(f"Coeffs: {coeffs}")
print("Equation: " +
    " => ".join([
        " + ".join([
            f'{i}{j}' for i, j in zip(ca[k], [
                "".join([
                    f'{key}{val}' if val != '1' else f'{key}' for key, val in i.items()
                ]) for i in componentsDict[0]
            ])
        ]) for k in [0,1]
    ]))
print("\n/////////////////////////")
