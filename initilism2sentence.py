import random

wordList = {"a": ["also ", "as ", "away "],
            "b": ["be ", "back ", "be", "by "],
            "c": ["course ", "cause "],
            "d": [],
            "e": [],
            "f": ["f ", "freak ", "from "],
            "g": ["gosh "],
            "h": ["head "],
            "i": ["I "],
            "j": [],
            "k": ["know ", "known ", "keyboard "],
            "l": ["later ", "let ", "le ", "love "],
            "m": ["my ", "me ", "mind "],
            "n": ["ne"],
            "o": ["oh ", "o"],
            "p": ["peo", "p", "possible "],
            "q": [],
            "r": ["right "],
            "s": ["shut ", "shaking ", "soon "],
            "t": ["talk ", "to ", "the "],
            "u": ["you ", "up "],
            "v": ["ver "],
            "w": ["way "],
            "x": [],
            "y": ["you "],
            "z": []}

def a2s(a,wordList):
    a = a.lower()
    result = ""
    for i in range(len(a)):
        result += wordList[a[i]][random.randint(0,len(wordList[a[i]])-1)]
    return result

test = ""
count = 0
while test != "oh my gosh ":
# for i in range(50):
    test = a2s("omg",wordList)
    count += 1
    print(count, test)
