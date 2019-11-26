import numpy as np

n = 3

# ZigZag
a = np.arange(0,n**2)
b = np.zeros((n,n))
for i in range(np.size(b,0)):
    for j in range(np.size(b,1)):
        if i % 2 == 0:
            b[i,j] = a[int(np.size(a)**(1/2))*i+j]
        else:
            b[i,int(np.size(a)**(1/2))-1-j] = a[int(np.size(a)**(1/2))*i+j]

print(b)

# Faster method
a = np.arange(n**2)
a.shape = (n,n)
for i in range(np.size(a,0)):
    if i % 2 != 0:
        a[i] = np.flip(a[i])
print(a)

#===============================================================================

# Popcorn
b = b.flatten()

def f(x):
    if x % 2 == 0:
        return x//2
    else:
        return -(x-((x-1)//2))

for i in range(np.size(b)):
    b[f(i)] = i

b.shape = (n,n)

print(b)
