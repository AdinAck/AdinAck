from english_words import english_words_lower_set

def get_wordle(known, not_allowed, must_contain):
    possible = []
    
    words = {
        word for word in english_words_lower_set
            if len(word) == len(known)
            and not any(
                letter in not_allowed for letter in word
            )
            and all(
                letter in word for letter in must_contain
            )
    }
    
    for word in words:
        if all(l1 == l2 for l1, l2 in zip(known, word) if l1 != '_'):
            possible.append(word)
    
    return possible

def main():
    known = input('Enter known letters (\'_\' if unknown): ')
    must_contain = input('Enter letters that must be in the word: ')
    not_allowed = input('Disallowed letters: ')
    
    print('Possible words:', end=' ')
    print(*get_wordle(known, not_allowed, must_contain), sep=', ')

if __name__ == "__main__":
    main()
