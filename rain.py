import numpy as np
from typing import *


def countRain(lst: List[int]) -> int:
    result: int = 0
    depth: int = max(lst)

    for _ in range(depth):
        lst = trimZeros(lst)
        for i in range(len(lst)):
            if lst[i] > 0:
                lst[i] -= 1
            else:
                result += 1
    return result


def trimZeros(lst: List[int]) -> List[int]:
    start: int = 0
    end: int = len(lst)

    for i, e in enumerate(lst):
        if e != 0:
            start = i
            break

    for i, e in enumerate(lst[::-1]):
        if e != 0:
            if i == 0:
                break
            end = -i
            break

    return lst[start:end]


if __name__ == "__main__":
    land = [0, 1, 2, 0, 1, 3, 2, 3, 1, 0, 1, 2, 3, 1, 2, 0]
    print(countRain(land))

    a = np.zeros((max(land), len(land)))
    for i, e in enumerate(land):
        a[-e:, i] = 1
    print(a)
