from typing import Any


def find(lst: list, c: Any) -> str:
    return (
        f"{c} is located at index(es) {', '.join(j)}."
        if len(j := [str(i) for i, e in enumerate(lst) if e == c]) > 0
        else
        f"{c} is not present."
    )


if __name__ == '__main__':
    ints = [0, 1, 2, 5, 4, 5, 6, 7, 8, 9]
    look = 5

    print(find(ints, look))

    strs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    look = 'h'

    print(find(strs, look))

    classes = [int, str, float, bool, list, dict, tuple, set, complex]
    look = None

    print(find(classes, look))
