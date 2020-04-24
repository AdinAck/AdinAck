# import time
# t = time.monotonic_ns()
a = [i[:-1] for i in list(open("diamond.in", "r"))]; b = [int(i) for i in a[1:]]
b = sorted(b); k = [int(i) for i in a[0].split()][-1]
c = [0]*(b[-1]-b[0]+1)
for i in range(len(b)):
    c[b[i]-b[0]] += 1
try:
    fr = max([sum(c[i:i+k+1]) for i in list(range(len(c)-k))])
except ValueError as e:
    fr = len(b)
    print("K is larger than dataset range, thus answer is equal to dataset length:",fr)
# print(time.monotonic_ns()-t)
f = open("diamond.out", "w")
f.write(str(fr))
f.close()
