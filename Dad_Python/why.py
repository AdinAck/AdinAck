# 2D array of variable size populated w/ integers counting up (ascending)
# organized like:

import numpy as np

n = 3
a = np.zeros((n**2))

print(a)

def f(x):
    if x % 2 == 0:
        return x//2
    else:
        return -(x-((x-1)//2))

for i in range(np.size(a)):
    print("place: " + str(f(i)) + "Number: " + str(i))
    a[f(i)] = i

print(a)
