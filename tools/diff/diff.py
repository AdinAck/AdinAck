import sys
from termcolor import colored

a = sys.argv[1]
b = sys.argv[2]

lut = {0: "green", 1: "yellow", 2: "red", 3: "white"}

excludedChars = [" "]


def printDiff(a, b, aoffset=0, boffset=0):
    diffText = []
    diffTable = []

    for i in range(max(len(a) + aoffset, len(b) + boffset)):
        c1 = aoffset <= i < len(a) + aoffset
        c2 = boffset <= i < len(b) + boffset
        if (c1 and a[i - aoffset] in excludedChars) or (
            c2 and b[i - boffset] in excludedChars
        ):
            diffTable.append(3)
            diffText.append(colored("-", lut[diffTable[i]]))
            continue
        if c1 and c2:
            if a[i - aoffset] == b[i - boffset]:
                diffTable.append(0)
                diffText.append(colored("=", lut[diffTable[i]]))
            else:
                diffTable.append(1)
                diffText.append(
                    colored(
                        "∨" if a[i - aoffset] > b[i - boffset] else "∧",
                        lut[diffTable[i]],
                    )
                )
        else:
            diffTable.append(2)
            diffText.append(colored("+", lut[diffTable[i]]))

    print(
        " " * aoffset
        + "".join(
            colored(char, lut[diffTable[i + aoffset]]) for i, char in enumerate(a)
        )
    )
    print("".join(diffText))
    print(
        " " * boffset
        + "".join(
            colored(char, lut[diffTable[i + boffset]]) for i, char in enumerate(b)
        )
    )


# sourcery skip: merge-else-if-into-elif
print("Direct comparison:")
printDiff(a, b)

print("\nPattern matching:")

if len(a) < len(b):
    small = a
    big = b
else:
    small = b
    big = a

top = [""] * (len(small) - 1) + [char for char in big] + [""] * (len(small) - 1)

res = []
offset = 0
for i in range(len(top) - len(small) + 1):
    tmp = sum(
        char1 == char2 if char1 not in excludedChars else False
        for char1, char2 in zip(small, top[i : i + len(small)])
    )
    res.append(tmp)

res = {key: val for key, val in zip(range(len(res)), res) if val == max(res)}

for i, key, val in zip(range(len(res)), res.keys(), res.values()):
    offset = key - len(small) + 1

    aoffset, boffset = 0, 0
    if offset >= 0:
        if big == a:
            boffset = offset
        else:
            aoffset = offset
    else:
        if big == b:
            boffset = -offset
        else:
            aoffset = -offset

    if i > 0:
        print(
            "-"
            * max(
                len(big) + (aoffset if big == a else boffset),
                len(small) + (aoffset if big == b else boffset),
            )
        )
    if small == a:
        print(" " * aoffset + str(aoffset))
    else:
        print(" " * boffset + str(boffset))
    printDiff(a, b, aoffset, boffset)
    if small == a:
        print(" " * (aoffset + len(a)) + str(aoffset + len(a)))
    else:
        print(" " * (boffset + len(b)) + str(boffset + len(b)))

    if i < len(res) - 1:
        print(
            "-"
            * max(
                len(big) + (aoffset if big == a else boffset),
                len(small) + (aoffset if big == b else boffset),
            ),
            end="\r",
        )
