import numpy as np

f = open("input.txt", 'r')
tmp = [i for i in f.read().split("\n") if i != ""]
t = int(tmp[0])
tmp = tmp[1:]
nkList = [[int(j) for j in i.split(" ")] for i in tmp[::2]]
sList = tmp[1::2]
print(t)
print(nkList)
print(sList)

def test(arr, slicee):
    return np.mean([int(k) for k in arr[slicee[0]:slicee[1]]])


for i in range(t):
    print(sList[i])
    count = len([k for k in sList[i] if k == "?"])
    print(count, nkList[i][1], sum([int(k) for k in sList[i] if k != "?"]))
