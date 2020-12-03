components = [[],[]]
# components = [['C H4', 'O2'], ['C O2', 'H2 O']]
# components = [['Ba Cl2', 'H2 S O4'], ['Ba S O4', 'H Cl']]
# components = [['Fe S2', 'O2'], ['Fe2 O3', 'S O2']]
# components = [['Fe2 O3', 'H2'], ['Fe', 'H']]
components = [['Al', 'Cu S O4'], ['Al2 S3 O12', 'Cu']]

# for i in range(2):
#     val = ""
#     print("Components:")
#     while val != "end":
#         val = input()
#         if val != "end":
#             components[i].append(val)
print(components)

# [['C H4', 'O2'], ['C O2', 'H2 O']]

# key: x + y = z + w

# step 0: get number of each element in each component

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

print(componentsDict)

# step 1: get a in relation to x
count1 = [key for key in componentsDict[0][0] for key2 in componentsDict[1][0] if key == key2]
if len(count1) > 1:
    print("idk how to solve this 1")
    exit()
z = lambda x: x * (int(componentsDict[0][0][count1[0]])/int(componentsDict[1][0][count1[0]]))

# step 2: get b in relation to x
count2 = [key for key in componentsDict[0][0] for key2 in componentsDict[1][1] if key == key2]
if len(count2) > 1:
    print("idk how to solve this 2")
    exit()
w = lambda x: x * (int(componentsDict[0][0][count2[0]])/int(componentsDict[1][1][count2[0]]))

# step 3: get y in relation to z and w
count3 = [key for key in componentsDict[0][1] for key2 in componentsDict[1][0] if key == key2]
tmp = []
for key in count3:
    tmp.append(int(componentsDict[0][1][key])/int(componentsDict[1][0][key]))
if len(tmp) != 0:
    if sum(tmp)/len(tmp) != tmp[0]:
        print("idk how to solve this 3")
        exit()

tmp = [count3[i] in [componentsDict[1][0], componentsDict[1][1]][j] for i in range(len(count3)) for j in range(2)]
print(tmp)
if len(tmp) > 2:
    if sum(tmp[::len(count3)]):
        y = lambda x: (int(componentsDict[1][0][count3[0]]) * z(x))/int(componentsDict[0][1][count3[0]])
    else:
        y = lambda x: (int(componentsDict[1][1][count3[0]]) * w(x))/int(componentsDict[0][1][count3[0]])
else:
    y = lambda x: (int(componentsDict[1][0][count3[0]]) * z(x) + int(componentsDict[1][1][count3[0]]) * w(x))/int(componentsDict[0][1][count3[0]])

for x in range(1,10):
    a = [x, y(x), z(x), w(x)]
    print(a)
    if sum([int(i) == i for i in a]) == 4 and len([int(i) for i in a if i == 0]) == 0:
        exit()
