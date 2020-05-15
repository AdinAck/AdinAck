# import time
# t = time.monotonic_ns()
a = [i[:-1] for i in list(open("diamond.in", "r"))]; b = [int(i) for i in a[1:]]
b = sorted(b); k = [int(i) for i in a[0].split()][-1]
c = [0]*(b[-1]-b[0]+1)
for i in range(len(b)):
    c[b[i]-b[0]] += 1
m = []
try:
    for j in range(2):
        r = list(range(len(c)-k))
        # for l in r:
        #     if len(c)>r.index(l)+k+2:
        #         if c[r.index(l)+k+1] == 0 and c[r.index(l)+k+2] == 0:
        #             r.pop(r.index(l))
        sums = [sum(c[i:i+k+1]) for i in r]
        fr, fri = max(sums),sums.index(max(sums))
        m.append(fr)
        c[fri:fri+k+1] = [0 for i in c[fri:fri+k+1]]
    final = sum(m)
except ValueError as e:
    final = len(b)
    print("K is larger than dataset range, thus answer is equal to dataset length:",final)
# print(time.monotonic_ns()-t)
f = open("diamond.out", "w")
f.write(str(final))
f.close()
