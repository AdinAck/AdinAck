k = 3
n = 4
x = 0
ops = 0
a = [1,2,1,3]

aMod = [i % k for i in a]

for i in a:
    if i != 0:
        i = k - i

aMod = sorted(aMod)




print(aMod)

i = 0
while True:
    if aMod[i] == 0:
        aMod.remove(0)
    elif x == aMod[i]:
        aMod[i] += x

    if i < len(aMod)-1:
        i += 1
    else:
        i = 0
    x += 1
    ops += 1


    break
