# 2D array of variable size populated w/ integers counting up (ascending)
# organized like:

import numpy as np

n = 4
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
a.shape = (n,n)
print(a)

################################################################################

a = np.zeroes((n**2))

def f(x):
    if

for i in range(np.size(a)):
