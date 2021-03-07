def fib(n, solved={0: 0, 1: 1}):
    if n-1 in solved:
        a = solved[n-1]
    else:
        a, solved = fib(n-1, solved)
        solved[n-1] = a

    if n-2 in solved:
        b = solved[n-2]
    else:
        b, solved = fib(n-2, solved)
        solved[n-2] = b

    return a+b, solved


print(fib(1000))
