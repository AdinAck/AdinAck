from random import uniform


def piFromRandom(size=10000):
    inCount = 0

    for _ in range(size):
        x, y = uniform(0, 1), uniform(0, 1)

        if (x**2+y**2)**(1/2) <= 1:
            inCount += 1

    return 4 * inCount/size


if __name__ == '__main__':
    for _ in range(10):
        print(piFromRandom())
