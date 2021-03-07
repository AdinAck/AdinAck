n = int(input())

for _ in range(n):
    input()
    arr = [int(i) for i in input().split(" ")]
    dic = {}

    for e in arr:
        if e not in dic:
            dic[e] = arr.count(e)

    lst = sorted(dic[key] for key in dic)
    l = len(lst);
    if l == 1:
        print(0)
        continue

    cumulative = [None]*(l-1)+[lst[-1]]
    for i in range(l-2, -1, -1):
        cumulative[i] = lst[i]+cumulative[i+1]

    previous = cumulative[1]-lst[0]*(l-1)
    result = previous

    for i in range(1, l-1):
        if lst[i] == lst[i-1]:
            continue

        a = cumulative[i+1]-lst[i]*(l-i-1)
        b = cumulative[0]-cumulative[i]

        previous = min(previous, a+b)

    if lst[-1] != lst[-2]:
        r = cumulative[0]-cumulative[l-1]
        previous = min(previous, r)

    print(previous)
