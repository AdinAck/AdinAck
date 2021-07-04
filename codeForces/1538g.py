def f(x, y, a, b):
    ma1 = max(x, y)
    mi1 = min(x, y)

    ma2 = max(a, b)
    mi2 = min(a, b)

    giftCount = 0

    while ma1 >= ma2 and mi1 >= mi2:
        step = min((mi1-ma1)//(mi2-ma2) + 1, ma1 //
                   ma2, mi1//mi2) if mi2 != ma2 else mi1
        # print(f'{step=}')
        giftCount += step

        # print(f'{ma1}\t{mi1}')
        # print(f'-{step*ma2}\t-{step*mi2}')

        ma1 -= step*ma2
        mi1 -= step*mi2

        _ma1 = max(ma1, mi1)
        mi1 = min(ma1, mi1)
        ma1 = _ma1

    # print(ma1, mi1)
    print(giftCount)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = [int(i) for i in input().split()]
        f(*a)
