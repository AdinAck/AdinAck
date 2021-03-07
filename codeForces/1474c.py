# Array Destruction
# 1700

import sys

def step(x, a, **kwargs):
    global solved
    if 'steps' in kwargs: steps = kwargs['steps']
    else: steps = []
    test1 = a[-1]
    test2 = x - test1
    if test1 not in solved:
        for i, num in enumerate(a[:-1]):
            if num == test2:
                solved[test1] = i
                a.pop(i)
                a.pop(-1)
                steps.append((test1, test2))
                if len(a) >= 2:
                    test1, _, _ = step(test1, a, steps=steps)
                break
    else:
        a.pop(solved[test1])
        a.pop(-1)
        steps.append((test1, test2))
        if len(a) >= 2:
            test1, _, _ = step(test1, a, steps=steps)

    return test1, len(a) == 0, steps

sys.setrecursionlimit(2000)

t = int(input())
for _ in range(t):
    try:
        n = input()
        a = sorted([int(num) for num in input().split(' ')])
        tmp = [i + a[-1] for i in a[:-1]]
        for num in tmp:
            solved = {}
            b = list(a)
            x, success, steps = step(num,b)
            if success:
                print('YES')
                print(num)
                [print(*step) for step in steps]
                break
        if not success:
            print('NO')
    except Exception as e:
        print(type(e), e)
