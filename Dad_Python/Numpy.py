import numpy as np

a = np.array([["A1","A2","A3"],
              ["B1","B1","B3"],
              ["C1","C2","C3"]])
print(a[2,0])

a[1][1] = "B2"
print(a)

a = a.flatten()
print(a)

a = np.zeros((10,2),dtype=int)

for i in range(np.size(a,0)):
    a[i,0] = i*17
    a[-(i+1),1] = i**5
print(a)

a = np.array(["a","b","c","d","e","f","g","h"])
print(a)
a.shape = (2,2,2)
print(a)
print(a[1,1,0])
a = np.insert(a,1,"",axis=2)
print(a)
